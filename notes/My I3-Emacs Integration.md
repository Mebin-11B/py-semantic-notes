---
title: "My I3-Emacs Integration"
url: https://khz.ac/software/i3-integration.html
clipped: 2026-06-17 00:58:28
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [My I3-Emacs Integration](https://khz.ac/software/i3-integration.html)

## Digest Summary
The i3 window manager intercepts all key events by calling `xcb_grab_key()` on the root window with `owner_events = 0`, causing i3 to capture keys before any client receives them. In `src/bindings.c` each binding’s keycode and modifier mask are passed to `xcb_grab_key(conn, 0, root, mods, keycode, XCB_GRAB_MODE_ASYNC, XCB_GRAB_MODE_ASYNC)`. When an XCB event arrives, `handle_event()` in `src/handlers.c` dispatches `XCB_KEY_PRESS`/`XCB_KEY_RELEASE` to `handle_key_press()` (src/key_press.c). This function extracts the keycode, timestamp, and state, looks up the corresponding `Binding` via `get_binding_from_xcb_event()`, and, if found, executes its command with `run_binding()`. The original `xcb_key_press_event_t` is available, allowing a potential re‑emit via `xcb_send_event()`. However, because i3 globally grabs keys, re‑emitting does not restore focus to the original window; addressing this focus loss would require additional changes beyond simple event forwarding.

## Discussion Summary
The discussion reflects a positive reception toward recent Hacker News stories featuring personal technical projects, such as Emacs–i3 integration, custom desk setups, and niche hobbyist creations. Participants express enthusiasm for these hands‑on, geek‑oriented demonstrations, emphasizing that while AI topics are appreciated, they do not dominate interest. There is a shared focus on practical window‑management solutions, exemplified by the adoption of an Emacs window‑manager bridge that leverages distinct keybindings for integrated control.

---

## Full Article

i3 uses `xcb_grab_key()` with `owner_events = 0` on the root x window to intercept
keys. the relevant code in `src/bindings.c` looks like
all unpatched code snippets refer to i3 4.25.1, if you want to follow
along.

```
172struct Binding_Keycode *binding_keycode;
173TAILQ_FOREACH(binding_keycode, &(bind->keycodes_head), keycodes) {
174    const int keycode = binding_keycode->keycode;
175    const int mods = (binding_keycode->modifiers & 0xFFFF);
176    DLOG("Binding %p Grabbing keycode %d with mods %d\n", bind, keycode, mods);
177    xcb_grab_key(conn, 0, root, mods, keycode, XCB_GRAB_MODE_ASYNC,
178                 XCB_GRAB_MODE_ASYNC);
179}
```

this code isn't super relevant, except that i3 entirely steals its bindings from
anyone else by intercepting on the *root* window. if you're thinking that setting
`owner_events = 1` to allow event passthrough so we don't have to re-emit… that
would be great, but that appears to instruct x to pass the event through to *only*
the root window. which is not what we want.

in i3's `handle_event()` in `src/handlers.c`, if it gets an xcb event, it sends it
off to a specialized handler based on its type:

```
1481switch (type) {
1482case XCB_KEY_PRESS:
1483case XCB_KEY_RELEASE:
1484    handle_key_press((xcb_key_press_event_t *)event);
1485    break;
1486    }
```

`handle_key_press()` (`src/key_press.c`) looks like this — it receives a keypress
event, looks up a binding based on that event, and, if it finds one, runs the
associated command:
yes, i do know one of the lines is too long. i opted to
leave it that way, as that's how it is in the i3 source. i should note, though:
i3 has really nice source code! i found it very readable and pleasant to work
inside.

```
12
18void handle_key_press(xcb_key_press_event_t *event) {
19    const bool key_release = (event->response_type == XCB_KEY_RELEASE);
20
21    last_timestamp = event->time;
22
23    DLOG("%s %d, state raw = 0x%x\n", (key_release ? "KeyRelease" : "KeyPress"), event->detail, event->state);
24
25    Binding *bind = get_binding_from_xcb_event((xcb_generic_event_t *)event);
26
27    
28    if (bind == NULL) {
29        return;
30    }
31
32    CommandResult *result = run_binding(bind, NULL);
33    command_result_free(result);
34}
```

notably, this function receives the original `xcb_key_press_event_t` from xcb,
which (after a bit of reading and experimentation) i realized you could just
re-emit diretly via `xcb_send_event()`.
unfortunately, the window receiving
the event will still lose focus, as i3 is intercepting key events globally. i
haven't fixed this; let me know if you know how.

this looks like a reasonable place to make a change!