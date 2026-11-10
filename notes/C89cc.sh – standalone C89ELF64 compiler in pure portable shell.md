---
title: "C89cc.sh – standalone C89/ELF64 compiler in pure portable shell"
url: https://gist.github.com/alganet/2b89c4368f8d23d033961d8a3deb5c19
clipped: 2026-06-17 01:23:35
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [C89cc.sh – standalone C89/ELF64 compiler in pure portable shell](https://gist.github.com/alganet/2b89c4368f8d23d033961d8a3deb5c19)

## Digest Summary
The repository “c89cc.sh” provides a self‑contained C89 compiler that generates ELF64 binaries using only portable shell scripts, without external toolchains. It implements the C89 language front‑end, parsing, code generation, and ELF64 output entirely within POSIX‑compatible shell code, enabling compilation on systems lacking a native compiler. The project includes example usage and documentation, and the GitHub page features contributor avatars labeled “@alganet” and “@lucaraymaekers”. The tool is positioned as a minimalistic, pure‑shell solution for building C programs in constrained environments.

## Discussion Summary
The remarks show cautious interest in the script, with a desire for safer execution through added tests, documentation, and a maintained repository rather than a simple gist. Users note its single‑file, tool‑free design, empty PATH, and claimed portability across several shells while producing x86 ELF binaries, yet there is confusion about whether it targets x86‑64 ELF or a generic shell. Despite uncertainty, the code’s apparent auto‑generation is widely regarded as impressively sophisticated. Overall, the feedback balances admiration with requests for better packaging and verification.

---

## Full Article

|  |  |
| --- | --- |
|  | #!/bin/sh |
|  | # ISC License |
|  |  |
|  | # Copyright (c) 2026 Alexandre Gomes Gaigalas <alganet@gmail.com> |
|  |  |
|  | # Permission to use, copy, modify, and/or distribute this software for any |
|  | # purpose with or without fee is hereby granted, provided that the above |
|  | # copyright notice and this permission notice appear in all copies. |
|  |  |
|  | # THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES |
|  | # WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF |
|  | # MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR |
|  | # ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES |
|  | # WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN |
|  | # ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF |
|  | # OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE. |
|  |  |
|  | # ============================================================ |
|  | # c89cc — standalone C89 parser + compiler (x86-64 ELF64) |
|  | # ============================================================ |
|  | # |
|  | # Usage: |
|  | # sh c89cc.sh < prog.c > a.out |
|  | # sh c89cc.sh --no-libc < prog.c > a.out (skip built-in libc) |
|  |  |
|  | # --- core/header.sh --- |
|  | set -euf |
|  | LC\_ALL=C |
|  | IFS='' |
|  | \_EOL=' |
|  | ' |
|  | \_TAB=" " |
|  | # Clear PATH: no external commands needed |
|  | PATH= |
|  | # Shell compat: aliases in bash, POSIX-like in zsh |
|  | shopt -s expand\_aliases >/dev/null 2>&1 || : |
|  | setopt sh\_word\_split null\_glob glob\_subst \ |
|  | no\_glob no\_multios no\_equals 2>/dev/null || : |
|  | # ksh/mksh fallback: 'local' may not exist, use 'typeset' instead |
|  | command -v local >/dev/null 2>&1 || alias local=typeset >/dev/null 2>&1 || : |
|  |  |
|  | # Fallback: if 'test' is not a builtin, wrap it via command -p |
|  | if ! command -v test >/dev/null 2>&1; then test () { command -p test "$@"; }; fi |
|  |  |
|  | # --- Output helpers --- |
|  | # Detect best available output primitive: |
|  | # printf > print > echo > command -p printf |
|  | # \_printn1: print string without newline \_printr1: print string with newline |
|  | if command -v printf >/dev/null 2>&1 |
|  | then |
|  | \_printn1 () { printf '%s' "$1"; } |
|  | \_printr1 () { printf '%s\n' "$@"; } |
|  | elif command -v print >/dev/null 2>&1 |
|  | then |
|  | \_printn1 () { echo -n -E "$1"; } |
|  | \_printr1 () { echo -E "$@"; } |
|  | elif command -v echo >/dev/null 2>&1 |
|  | then |
|  | \_printn1 () { echo -n "$1"; } |
|  | \_printr1 () { echo "$@"; } |
|  | else |
|  | # yash fallback |
|  | \_printn1 () { command -p printf '%s' "$1"; } |
|  | \_printr1 () { command -p printf '%s\n' "$@"; } |
|  | fi |
|  |  |
|  | # --- Multi-value return and dynamic local variable helpers --- |
|  | # Pack variable assignments into REPLY (append mode). |
|  | # Caller unpacks with: eval "$REPLY" (sets globals) |
|  | # or: eval "local$REPLY" (sets locals) |
|  | # Values containing ' must be pre-escaped with \_esc\_sq. |
|  | # Usage: REPLY=; \_retv name val; \_retva prefix idx val; eval "local$REPLY" |
|  | \_retv () { REPLY="$REPLY $1='$2'"; } |
|  | \_retva () { REPLY="$REPLY ${1}\_${2}='$3'"; } |
|  |  |
|  | # --- module system (stub, all modules inlined) --- |
|  | \_MOD="$\_EOL" |
|  | \_mod\_has () { return 0; } |
|  | \_mod\_add () { :; } |
|  | use () { :; } |
|  |  |
|  | # --- modules/str/repeat.sh --- |
|  | # Repeat a string N times via exponentiation-by-squaring. |
|  | \_repeat () { |
|  | case "${2:-}" in |
|  | 0|"") return;; 1) REPLY="$1"; return;; 2) REPLY="$1$1"; return;; |
|  | 3) REPLY="$1$1$1"; return;; 4) REPLY="$1$1$1$1"; return;; |
|  | esac |
|  | local VALUE="$1" COUNT="$2" POW=2; REPLY= |
|  | while :; do |
|  | if test $POW -gt $COUNT; then |
|  | test $COUNT -gt 0 || break |
|  | REPLY="$REPLY$VALUE" VALUE="$1" |
|  | COUNT=$((COUNT - (POW / 2))) POW=2 |
|  | continue; fi |
|  | VALUE="$VALUE$VALUE" POW=$((POW \* 2)) |
|  | done |
|  | } |
|  |  |
|  | # Memoized '???...?' pattern generator (used to split long input lines). |
|  | \_questn () { |
|  | eval "case \${\_questn$1:-} in \"\") |
|  | \_repeat \\? $1; \_questn$1=\$REPLY |
|  | ;; esac; REPLY=\$\_questn$1" |
|  | } |
|  |  |
|  | # --- modules/str/core.sh --- |
|  | # Convert string to uppercase (a-z → A-Z). Result in REPLY. |
|  | \_ucase () { |
|  | local \_s="$1" \_r= \_c |
|  | while test ${#\_s} -gt 0; do |
|  | \_c="${\_s%"${\_s#?}"}"; \_s="${\_s#?}" |
|  | case "$\_c" in |
|  | a) \_r="${\_r}A";; b) \_r="${\_r}B";; c) \_r="${\_r}C";; |
|  | d) \_r="${\_r}D";; e) \_r="${\_r}E";; f) \_r="${\_r}F";; |
|  | g) \_r="${\_r}G";; h) \_r="${\_r}H";; i) \_r="${\_r}I";; |
|  | j) \_r="${\_r}J";; k) \_r="${\_r}K";; l) \_r="${\_r}L";; |
|  | m) \_r="${\_r}M";; n) \_r="${\_r}N";; o) \_r="${\_r}O";; |
|  | p) \_r="${\_r}P";; q) \_r="${\_r}Q";; r) \_r="${\_r}R";; |
|  | s) \_r="${\_r}S";; t) \_r="${\_r}T";; u) \_r="${\_r}U";; |
|  | v) \_r="${\_r}V";; w) \_r="${\_r}W";; x) \_r="${\_r}X";; |
|  | y) \_r="${\_r}Y";; z) \_r="${\_r}Z";; |
|  | \*) \_r="${\_r}${\_c}";; |
|  | esac |
|  | done |
|  | REPLY="$\_r" |
|  | } |
|  |  |
|  | # Convert uppercase char to lowercase. Result in REPLY. |
|  | \_lcase () { |
|  | case "$1" in A) REPLY=a;; B) REPLY=b;; C) REPLY=c;; D) REPLY=d;; |
|  | E) REPLY=e;; F) REPLY=f;; G) REPLY=g;; H) REPLY=h;; |
|  | I) REPLY=i;; J) REPLY=j;; K) REPLY=k;; L) REPLY=l;; |
|  | M) REPLY=m;; N) REPLY=n;; O) REPLY=o;; P) REPLY=p;; |
|  | Q) REPLY=q;; R) REPLY=r;; S) REPLY=s;; T) REPLY=t;; |
|  | U) REPLY=u;; V) REPLY=v;; W) REPLY=w;; X) REPLY=x;; |
|  | Y) REPLY=y;; Z) REPLY=z;; \*) REPLY=;; esac |
|  | } |
|  |  |
|  | # Convert uppercase string to lowercase. Result in REPLY. |
|  | \_lcase\_str () { |
|  | local \_s="$1" \_c \_r= |
|  | while test ${#\_s} -gt 0; do |
|  | \_c="${\_s%"${\_s#?}"}"; \_s="${\_s#?}" |
|  | \_lcase "$\_c" |
|  | case "$REPLY" in '') \_r="$\_r$\_c";; \*) \_r="$\_r$REPLY";; esac |
|  | done |
|  | REPLY="$\_r" |
|  | } |
|  |  |
|  | # --- modules/io/readall.sh --- |
|  | # Read all of stdin into REPLY (replaces /bin/cat for eval "$(\_readall)"). |
|  | \_readall () { |
|  | REPLY= |
|  | while IFS='' read -r \_l; do REPLY="$REPLY$\_l$\_EOL"; done |
|  | REPLY="$REPLY$\_l" |
|  | } |
|  |  |
|  | # --- modules/pos/core.sh --- |
|  | # Count newlines in a consumed/skipped string, update \_LN/\_COL. |
|  | # No-newline fast path: just adds string length to \_COL. |
|  | \_nlcount () { |
|  | local \_s="$1" \_h |
|  | case "$\_s" in \*"$\_EOL"\*) |
|  | while :; do |
|  | \_h="${\_s#\*"$\_EOL"}" |
|  | case "$\_h" in \*"$\_EOL"\*) |
|  | \_LN=$((\_LN+1)); \_s="$\_h";; |
|  | \*) |
|  | \_LN=$((\_LN+1)) |
|  | \_COL=$((${#\_h} + 1)) |
|  | return;; |
|  | esac |
|  | done;; |
|  | \*) |
|  | \_COL=$((\_COL + ${#\_s}));; |
|  | esac |
|  | } |
|  |  |
|  | # Validate CONSUMED as RFC 8259 number: [-](0|[1-9]d\*)[.d+][eE[+-]d+] |
|  | \_numck () { |
|  | local \_n="$CONSUMED" |
|  | case "$\_n" in '-'\*) \_n="${\_n#-}";; esac |
|  | case "$\_n" in |
|  | '') \_error NUMBER;; |
|  | '0'[0-9]\*) \_error NUMBER;; |
|  | '0'\*) \_n="${\_n#0}";; |
|  | [1-9]\*) \_n="${\_n#[1-9]}"; \_n="${\_n#"${\_n%%[!0-9]\*}"}";; |
|  | \*) \_error NUMBER;; |
|  | esac |
|  | case "$\_n" in '.'\*) |
|  | \_n="${\_n#.}" |
|  | case "$\_n" in [0-9]\*) ;; \*) \_error NUMBER;; esac |
|  | \_n="${\_n#"${\_n%%[!0-9]\*}"}";; |
|  | esac |
|  | case "$\_n" in [eE]\*) |
|  | \_n="${\_n#?}" |
|  | case "$\_n" in '+'\*|'-'\*) \_n="${\_n#?}";; esac |
|  | case "$\_n" in [0-9]\*) ;; \*) \_error NUMBER;; esac |
|  | \_n="${\_n#"${\_n%%[!0-9]\*}"}";; |
|  | esac |
|  | case "$\_n" in '') ;; \*) \_error NUMBER;; esac |
|  | } |
|  |  |
|  | # --- modules/err/core.sh --- |
|  |  |
|  | \_error () { |
|  | IFS=' ' |
|  | eval "\_a=\"\${\_SRC$\_LN:-}\"" |
|  | \_printr1 "$\* at $\_LN:$\_COL" |
|  | case "$\_a" in ?\*) |
|  | \_printr1 " $\_a" |
|  | \_repeat ' ' $\_COL; \_printr1 " ${REPLY}^" |
|  | ;; esac |
|  | exit 1 |
|  | } |
|  |  |
|  | # --- modules/ast/core.sh --- |
|  |  |
|  | # --- Input feeding --- |
|  | # Read from stdin into CODE buffer, one line at a time. |
|  | # Lines > 128 chars are split into chunks before appending. |
|  | # ast\_read: read one line, chunk-split into CODE |
|  | # ast\_feed: refill when CODE < 16 chars (tight loop, most branches) |
|  | # ast\_more: refill when CODE < 1024 chars (bulk reads for names/keywords) |
|  | alias ast\_read='if IFS= read -r \_line |
|  | then |
|  | \_RD=$((\_RD + 1)); eval "\_SRC$\_RD=\"\$\_line\"" |
|  | while test ${#\_line} -gt 128; do |
|  | \_questn 128 |
|  | \_b="${\_line#${REPLY}}"; \_a="${\_line%"$\_b"}" |
|  | CODE="$CODE$\_a"; \_line="$\_b" |
|  | done |
|  | CODE="$CODE$\_line$\_EOL" |
|  | else \_EOF=1; CODE="$CODE$\_line" |
|  | case "$\_line" in ?\*) \_RD=$((\_RD + 1)); eval "\_SRC$\_RD=\"\$\_line\"";; esac |
|  | fi' |
|  |  |
|  | alias ast\_feed='if test ${#CODE} -lt 16 -a $\_EOF -eq 0; then ast\_read; fi' |
|  | alias ast\_more=' |
|  | while test ${#CODE} -lt 1024 -a $\_EOF -eq 0 |
|  | do ast\_read; done' |
|  |  |
|  | # --- Character-level operations --- |
|  | # ast\_consume - move 1-4 chars from CODE into CONSUMED |
|  | # ast\_skip - discard 1-3 chars or whitespace from CODE |
|  | # \_ast\_xfer - base: append stripped prefix to CONSUMED |
|  | # \_ast\_xbulk - base: append REST to CONSUMED, advance CODE |
|  | alias \_ast\_xfer='CONSUMED="$CONSUMED${CODE%"$REST"}"; CODE="$REST"' |
|  | alias \_ast\_xbulk='CONSUMED="$CONSUMED$REST"; CODE="${CODE#"$REST"}"' |
|  | alias ast\_consume='REST="${CODE#?}"; \_ast\_xfer; \_COL=$((\_COL+1))' |
|  | alias ast\_consume2='REST="${CODE#??}"; \_ast\_xfer; \_COL=$((\_COL+2))' |
|  | alias ast\_consume3='REST="${CODE#???}"; \_ast\_xfer; \_COL=$((\_COL+3))' |
|  | alias ast\_consume4='REST="${CODE#????}"; \_ast\_xfer; \_COL=$((\_COL+4))' |
|  |  |
|  | alias ast\_skip='CODE="${CODE#?}"; \_COL=$((\_COL+1))' |
|  | alias ast\_skip2='CODE="${CODE#??}"; \_COL=$((\_COL+2))' |
|  | alias ast\_skip3='CODE="${CODE#???}"; \_COL=$((\_COL+3))' |
|  | alias \_ast\_advcol='\_COL=$((\_COL+${#REST}))' |
|  | alias ast\_skip\_ws='REST="${CODE%%[! $\_TAB]\*}"; \_ast\_advcol; CODE="${CODE#"$REST"}"' |
|  | alias ast\_skip\_wse='REST="${CODE%%[! $\_TAB$\_EOL]\*}" |
|  | CODE="${CODE#"$REST"}"; \_nlcount "$REST"' |
|  | # Newline-aware variants |
|  | alias ast\_skip\_nl='CODE="${CODE#?}"; \_LN=$((\_LN+1)); \_COL=1' |
|  | alias ast\_skip2\_nl='CODE="${CODE#??}"; \_LN=$((\_LN+1)); \_COL=1' |
|  | alias ast\_consume\_nl='REST="${CODE#?}"; \_ast\_xfer; \_LN=$((\_LN+1)); \_COL=1' |
|  | # ast\_bulk - append REST to CONSUMED, advance CODE, loop |
|  | alias ast\_bulk='\_ast\_xbulk; \_ast\_advcol; continue' |
|  | alias ast\_bulk\_nl='\_ast\_xbulk; \_nlcount "$REST"; continue' |
|  |  |
|  | # --- AST stack operations --- |
|  | # ast\_new - push state, save CONSUMED as V<n>, reset CONSUMED |
|  | # ast\_push - create tree node X<n>=<state>, push index onto NODES stack |
|  | # ast\_pop - pop state + node stacks |
|  | # Primitives (used by composed aliases below): |
|  | # ast\_attach - attach node to parent |
|  | # ast\_collapse - collapse single-valueless-child wrapper into the child |
|  | # pars\_attach\_op - ast\_attach + operator-precedence: if prev sibling is Ab/Ob/Pb/Bu, |
|  | # restructure so the operator steals the prev sibling |
|  | # Composed close operations (all start with ast\_pop): |
|  | # ast\_discard - ast\_pop + discard (for transient states like Cs) |
|  | # ast\_close - ast\_pop + ast\_attach |
|  | # pars\_close\_op - ast\_pop + pars\_attach\_op |
|  | # ast\_close\_col - ast\_pop + ast\_collapse + ast\_attach |
|  | # pars\_close\_op\_col - ast\_pop + ast\_collapse + pars\_attach\_op |
|  | # pars\_close\_redir - ast\_close + error if redirect target is empty |
|  | # ast\_flush - flush CONSUMED as Tx child (a"b"c) |
|  | alias ast\_new='STATES="$STATES $STATE"; V=$((V + 1)) |
|  | case "$CONSUMED" in "");; \*) local V$V="$CONSUMED";;esac |
|  | CONSUMED=' |
|  | alias ast\_push='local X$V="$STATE" |
|  | PARN="${NODES##\*" "}" |
|  | eval "PARNT=\"\${X$PARN%% \*}\"" |
|  | NODE=$V; NODES="$NODES $NODE"' |
|  | alias ast\_pop='STATE="${STATES##\*" "}"; STATES="${STATES%" ${STATE}"}" |
|  | PARN="${NODES##\*" "}" |
|  | case "$CONSUMED" in ?\*) local V$PARN="$CONSUMED";; esac |
|  | CONSUMED= |
|  | NODE=$PARN; NODES="${NODES%" $NODE"}"; PARN="${NODES##\*" "}" |
|  | eval "PARNT=\"\${X$PARN%% \*}\""' |
|  |  |
|  | alias ast\_attach='eval "X$PARN=\"\$X$PARN \$NODE\""' |
|  | alias ast\_collapse='eval "\_D=\"\$X$NODE\""; \_C="${\_D#\* }" |
|  | case "$\_C" in "$\_D"|\*" "\*) ;; |
|  | \*) eval "case \"\${V$NODE:-}\" in \"\") unset X$NODE; NODE=$\_C;; esac";; |
|  | esac' |
|  | alias ast\_discard='ast\_pop;unset X$NODE' |
|  | alias ast\_close='ast\_pop;ast\_attach' |
|  | alias ast\_close\_col='ast\_pop;ast\_collapse;ast\_attach' |
|  | alias ast\_flush='case "$CONSUMED" in ?\*) ast\_Tx;ast\_close;; esac' |
|  |  |
|  | # Register AST node types. Each type gets an ast\_XX alias |
|  | # that creates a new node, sets STATE, and pushes onto the stack. |
|  | # Register AST node types. Outputs alias definitions to be eval'd. |
|  | # Usage: eval "$(ast\_tokens "Ty Pe Na Me")" |
|  | ast\_tokens () { |
|  | IFS=' ' |
|  | for \_s in $1; do |
|  | \_printr1 "alias ast\_$\_s=\"ast\_new;STATE=$\_s;ast\_push\"" |
|  | done |
|  | IFS='' |
|  | } |
|  |  |
|  | # Walk the AST from root, printing V<n> (value) and X<n> (node) in tree order. |
|  | # Format: X<n>='<type> [<child\_indices>...]' V<n>='<value>' |
|  | # Uses dynamic scoping to access caller's V<n>/X<n> locals. |
|  | ast\_out () { |
|  | set -- 0 |
|  | while test $# -gt 0; do |
|  | NODE=$1; shift |
|  | eval "\_pq=\"\${V$NODE:-}\"; \_D=\"\$X$NODE\"" |
|  | case "$\_pq" in ?\*) |
|  | # Escape single quotes in values: 'abc'd'ef' -> 'abc'\''ef' |
|  | case "$\_pq" in \*"'"\*) |
|  | \_printn1 "V$NODE=" |
|  | while :; do |
|  | case "$\_pq" in \*"'"\*) ;; \*) break;; esac |
|  | \_printn1 "'${\_pq%%"'"\*}'\\'"; \_pq="${\_pq#\*"'"}" |
|  | done |
|  | \_printn1 "'$\_pq'$\_EOL";; |
|  | \*) \_printr1 "V$NODE='$\_pq'";; |
|  | esac;; esac |
|  | \_printr1 "X$NODE='$\_D'" |
|  | \_C="${\_D#\* }" |
|  | case "$\_C" in "$\_D") ;; ?\*) |
|  | IFS=' '; set -- $\_C "$@"; IFS='' |
|  | ;; esac |
|  | done |
|  | } |
|  |  |
|  | # --- Progress check (loop detection) --- |
|  | # Two-level check: |
|  | # 1. Exact repeat (same CODE length + state + position) → immediate error |
|  | # 2. No input consumed for 4096 iterations → stuck in state cycle |
|  | alias pars\_progress='case "${#CODE}.$STATE.$\_LN.$\_COL" in "$\_PREV") \_error INTERNAL LOOP;; esac; \_PREV="${#CODE}.$STATE.$\_LN.$\_COL"; case ${#CODE} in "$\_PLEN") \_PLC=$((\_PLC+1)); case $((\_PLC>4096)) in 1) \_error INTERNAL LOOP;; esac;; \*) \_PLEN=${#CODE}; \_PLC=0;; esac' |
|  |  |
|  | # --- Error reporting helpers --- |
|  | alias \_pars\_err='eval "\_a=\"\${\_EXP\_$STATE:-token}\""; \_error "expected: $\_a"' |
|  | alias \_pars\_err\_eof='eval "\_a=\"\${\_EXP\_$STATE:-token}\""; \_error "unexpected end of input, expected: $\_a"' |
|  |  |
|  | # --- Parser epilogue (emitter wrappers, footer, dispatch) --- |
|  | # $1=grammar name, $2=script arg (optional command override). |
|  | # Called after the emitter function is defined. |
|  | \_ast\_core\_pars\_epilogue () { |
|  | eval "\_emit\_${1}\_root () { \_emit\_$1 \"\$@\"; }" |
|  | . "$\_DIR/core/footer.sh" |
|  | eval "unast\_$1 () { \_readall; eval \"\$REPLY\"; \_emit\_${1}\_root 0; \_printr1 \"\$REPLY\"; }" |
|  | eval "reast\_$1 () { pars\_$1 | unast\_$1; }" |
|  | case "${PARS\_LIB:-}" in "") |
|  | case "${2:-}" in |
|  | "") "pars\_$1";; |
|  | pars\_\*|unast\_\*|reast\_\*) $2;; |
|  | \*) \_printr1 "usage: $0 [pars\_$1 | unast\_$1 | reast\_$1]" |
|  | \_printr1 " pars\_$1 parse stdin, print AST (default)" |
|  | \_printr1 " unast\_$1 read AST from stdin, print source" |
|  | \_printr1 " reast\_$1 parse stdin, print source (round-trip)" |
|  | exit 1;; |
|  | esac |
|  | ;; esac |
|  | } |
|  |  |
|  | # --- modules/ast/consume.sh --- |
|  | # --- Match/operator consumption --- |
|  | # Used by parsers with keyword matching or precedence climbing. |
|  | # Skip MATCH from CODE (keyword skip after case-insensitive match) |
|  | alias ast\_skip\_match='CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH}))' |
|  | # Consume MATCH into CONSUMED (keyword consumed as AST value) |
|  | alias ast\_consume\_match='CONSUMED="$MATCH"; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH}))' |
|  | # Consume \_OP into CONSUMED (binary operator consumption) |
|  | alias ast\_consume\_op='CONSUMED="$\_OP"; CODE="${CODE#"$\_OP"}"; \_COL=$((\_COL+${#\_OP}))' |
|  |  |
|  | # --- modules/ast/prec.sh --- |
|  | # --- Precedence climbing helpers --- |
|  | # Used by parsers with #!precedence directives. |
|  | # Close node and re-enter precedence climbing loop. |
|  | alias ast\_close\_xc='ast\_close; \_XC=1; \_PREV=; continue' |
|  | alias ast\_close\_col\_xc='ast\_close\_col; \_XC=1; \_PREV=; continue' |
|  |  |
|  | # --- modules/ast/comment.sh --- |
|  | # --- Comment skip --- |
|  | # Used by parsers with #!comment directives. |
|  | # Requires variables set by the generated parser: |
|  | # \_CMT\_S, \_CMT\_SL -- block comment start marker and its length |
|  | # \_CMT\_E, \_CMT\_EL -- block comment end marker and its length |
|  |  |
|  | # Line comment: skip from current position to end of line |
|  | alias ast\_cmt\_line='REST="${CODE%%"$\_EOL"\*}" |
|  | CODE="${CODE#"$REST"}" |
|  | \_COL=$((\_COL+${#REST})); continue' |
|  |  |
|  | # Block comment: skip from start marker to end marker, counting newlines |
|  | alias ast\_cmt\_block='CODE="${CODE#"$\_CMT\_S"}"; \_COL=$((\_COL+\_CMT\_SL)) |
|  | while :; do |
|  | case "$CODE" in \*"$\_CMT\_E"\*) |
|  | REST="${CODE%%"$\_CMT\_E"\*}" |
|  | \_nlcount "$REST" |
|  | CODE="${CODE#"$REST"}"; CODE="${CODE#"$\_CMT\_E"}" |
|  | \_COL=$((\_COL+\_CMT\_EL)); break;; |
|  | \*) case $\_EOF in 1) \_error "unclosed comment";; esac |
|  | \_nlcount "$CODE"; CODE=; ast\_read;; |
|  | esac |
|  | done; continue' |
|  |  |
|  | # --- modules/c89/parser.sh --- |
|  |  |
|  | alias ast\_Ca="ast\_new;STATE=Ca;ast\_push" |
|  | alias ast\_Cb="ast\_new;STATE=Cb;ast\_push" |
|  | alias ast\_Cc="ast\_new;STATE=Cc;ast\_push" |
|  | alias ast\_Cd="ast\_new;STATE=Cd;ast\_push" |
|  | alias ast\_Ce="ast\_new;STATE=Ce;ast\_push" |
|  | alias ast\_Cf="ast\_new;STATE=Cf;ast\_push" |
|  | alias ast\_Cg="ast\_new;STATE=Cg;ast\_push" |
|  | alias ast\_Ch="ast\_new;STATE=Ch;ast\_push" |
|  | alias ast\_Ci="ast\_new;STATE=Ci;ast\_push" |
|  | alias ast\_Cj="ast\_new;STATE=Cj;ast\_push" |
|  | alias ast\_Ck="ast\_new;STATE=Ck;ast\_push" |
|  | alias ast\_Cl="ast\_new;STATE=Cl;ast\_push" |
|  | alias ast\_Cm="ast\_new;STATE=Cm;ast\_push" |
|  | alias ast\_Cn="ast\_new;STATE=Cn;ast\_push" |
|  | alias ast\_Co="ast\_new;STATE=Co;ast\_push" |
|  | alias ast\_Cp="ast\_new;STATE=Cp;ast\_push" |
|  | alias ast\_Cq="ast\_new;STATE=Cq;ast\_push" |
|  | alias ast\_Cr="ast\_new;STATE=Cr;ast\_push" |
|  | alias ast\_Cs="ast\_new;STATE=Cs;ast\_push" |
|  | alias ast\_Ct="ast\_new;STATE=Ct;ast\_push" |
|  | alias ast\_Cu="ast\_new;STATE=Cu;ast\_push" |
|  | alias ast\_Cv="ast\_new;STATE=Cv;ast\_push" |
|  | alias ast\_Cw="ast\_new;STATE=Cw;ast\_push" |
|  | alias ast\_Cx="ast\_new;STATE=Cx;ast\_push" |
|  | alias ast\_Cy="ast\_new;STATE=Cy;ast\_push" |
|  | alias ast\_Cz="ast\_new;STATE=Cz;ast\_push" |
|  | alias ast\_C1="ast\_new;STATE=C1;ast\_push" |
|  | alias ast\_C2="ast\_new;STATE=C2;ast\_push" |
|  | alias ast\_C3="ast\_new;STATE=C3;ast\_push" |
|  | alias ast\_C4="ast\_new;STATE=C4;ast\_push" |
|  | alias ast\_C5="ast\_new;STATE=C5;ast\_push" |
|  | alias ast\_C6="ast\_new;STATE=C6;ast\_push" |
|  | alias ast\_C7="ast\_new;STATE=C7;ast\_push" |
|  | alias ast\_C8="ast\_new;STATE=C8;ast\_push" |
|  | alias ast\_C9="ast\_new;STATE=C9;ast\_push" |
|  | alias ast\_C10="ast\_new;STATE=C10;ast\_push" |
|  | alias ast\_C11="ast\_new;STATE=C11;ast\_push" |
|  | alias ast\_C12="ast\_new;STATE=C12;ast\_push" |
|  | alias ast\_C13="ast\_new;STATE=C13;ast\_push" |
|  | alias ast\_C14="ast\_new;STATE=C14;ast\_push" |
|  | alias ast\_C15="ast\_new;STATE=C15;ast\_push" |
|  | alias ast\_C16="ast\_new;STATE=C16;ast\_push" |
|  | alias ast\_C17="ast\_new;STATE=C17;ast\_push" |
|  | alias ast\_C18="ast\_new;STATE=C18;ast\_push" |
|  | alias ast\_C19="ast\_new;STATE=C19;ast\_push" |
|  | alias ast\_C20="ast\_new;STATE=C20;ast\_push" |
|  | alias ast\_C21="ast\_new;STATE=C21;ast\_push" |
|  | alias ast\_C22="ast\_new;STATE=C22;ast\_push" |
|  | alias ast\_C23="ast\_new;STATE=C23;ast\_push" |
|  | alias ast\_C24="ast\_new;STATE=C24;ast\_push" |
|  | alias ast\_C25="ast\_new;STATE=C25;ast\_push" |
|  | alias ast\_C26="ast\_new;STATE=C26;ast\_push" |
|  | alias ast\_C27="ast\_new;STATE=C27;ast\_push" |
|  | alias ast\_C28="ast\_new;STATE=C28;ast\_push" |
|  | alias ast\_C29="ast\_new;STATE=C29;ast\_push" |
|  | alias ast\_C30="ast\_new;STATE=C30;ast\_push" |
|  | alias ast\_C31="ast\_new;STATE=C31;ast\_push" |
|  | alias ast\_C32="ast\_new;STATE=C32;ast\_push" |
|  | alias ast\_C33="ast\_new;STATE=C33;ast\_push" |
|  | alias ast\_C34="ast\_new;STATE=C34;ast\_push" |
|  | alias ast\_C35="ast\_new;STATE=C35;ast\_push" |
|  | alias ast\_C36="ast\_new;STATE=C36;ast\_push" |
|  | alias ast\_C37="ast\_new;STATE=C37;ast\_push" |
|  | alias ast\_C38="ast\_new;STATE=C38;ast\_push" |
|  | alias ast\_C39="ast\_new;STATE=C39;ast\_push" |
|  | alias ast\_C40="ast\_new;STATE=C40;ast\_push" |
|  | alias ast\_C41="ast\_new;STATE=C41;ast\_push" |
|  | alias ast\_C42="ast\_new;STATE=C42;ast\_push" |
|  | alias ast\_C43="ast\_new;STATE=C43;ast\_push" |
|  | alias ast\_C44="ast\_new;STATE=C44;ast\_push" |
|  | alias ast\_C45="ast\_new;STATE=C45;ast\_push" |
|  | alias ast\_C46="ast\_new;STATE=C46;ast\_push" |
|  | alias ast\_C47="ast\_new;STATE=C47;ast\_push" |
|  | alias ast\_C48="ast\_new;STATE=C48;ast\_push" |
|  | alias ast\_C49="ast\_new;STATE=C49;ast\_push" |
|  | alias ast\_C50="ast\_new;STATE=C50;ast\_push" |
|  | alias ast\_C51="ast\_new;STATE=C51;ast\_push" |
|  | alias ast\_C52="ast\_new;STATE=C52;ast\_push" |
|  | alias ast\_C53="ast\_new;STATE=C53;ast\_push" |
|  | alias ast\_C54="ast\_new;STATE=C54;ast\_push" |
|  | alias ast\_C55="ast\_new;STATE=C55;ast\_push" |
|  | alias ast\_C56="ast\_new;STATE=C56;ast\_push" |
|  | alias ast\_C57="ast\_new;STATE=C57;ast\_push" |
|  | alias ast\_C58="ast\_new;STATE=C58;ast\_push" |
|  | alias ast\_C59="ast\_new;STATE=C59;ast\_push" |
|  | alias ast\_C60="ast\_new;STATE=C60;ast\_push" |
|  | alias ast\_C61="ast\_new;STATE=C61;ast\_push" |
|  | alias ast\_C62="ast\_new;STATE=C62;ast\_push" |
|  | alias ast\_C63="ast\_new;STATE=C63;ast\_push" |
|  | alias ast\_C64="ast\_new;STATE=C64;ast\_push" |
|  | alias ast\_C65="ast\_new;STATE=C65;ast\_push" |
|  | alias ast\_C66="ast\_new;STATE=C66;ast\_push" |
|  | alias ast\_C67="ast\_new;STATE=C67;ast\_push" |
|  | alias ast\_C68="ast\_new;STATE=C68;ast\_push" |
|  | alias ast\_C69="ast\_new;STATE=C69;ast\_push" |
|  | alias ast\_C70="ast\_new;STATE=C70;ast\_push" |
|  | alias ast\_C71="ast\_new;STATE=C71;ast\_push" |
|  | alias ast\_C72="ast\_new;STATE=C72;ast\_push" |
|  | alias ast\_C73="ast\_new;STATE=C73;ast\_push" |
|  | alias ast\_C74="ast\_new;STATE=C74;ast\_push" |
|  | alias ast\_C75="ast\_new;STATE=C75;ast\_push" |
|  | alias ast\_C76="ast\_new;STATE=C76;ast\_push" |
|  | alias ast\_C77="ast\_new;STATE=C77;ast\_push" |
|  | alias ast\_C78="ast\_new;STATE=C78;ast\_push" |
|  | alias ast\_C79="ast\_new;STATE=C79;ast\_push" |
|  | alias ast\_C80="ast\_new;STATE=C80;ast\_push" |
|  | alias ast\_C81="ast\_new;STATE=C81;ast\_push" |
|  | alias ast\_C82="ast\_new;STATE=C82;ast\_push" |
|  | alias ast\_C83="ast\_new;STATE=C83;ast\_push" |
|  | alias ast\_C84="ast\_new;STATE=C84;ast\_push" |
|  | alias ast\_C85="ast\_new;STATE=C85;ast\_push" |
|  | alias ast\_C86="ast\_new;STATE=C86;ast\_push" |
|  | alias ast\_C87="ast\_new;STATE=C87;ast\_push" |
|  | alias ast\_C88="ast\_new;STATE=C88;ast\_push" |
|  | alias ast\_C89="ast\_new;STATE=C89;ast\_push" |
|  | alias ast\_C90="ast\_new;STATE=C90;ast\_push" |
|  | alias ast\_C91="ast\_new;STATE=C91;ast\_push" |
|  | alias ast\_C92="ast\_new;STATE=C92;ast\_push" |
|  | alias ast\_C93="ast\_new;STATE=C93;ast\_push" |
|  | alias ast\_C94="ast\_new;STATE=C94;ast\_push" |
|  | alias ast\_C95="ast\_new;STATE=C95;ast\_push" |
|  | alias ast\_C96="ast\_new;STATE=C96;ast\_push" |
|  | alias ast\_C97="ast\_new;STATE=C97;ast\_push" |
|  | alias ast\_C98="ast\_new;STATE=C98;ast\_push" |
|  | alias ast\_C99="ast\_new;STATE=C99;ast\_push" |
|  | alias ast\_C100="ast\_new;STATE=C100;ast\_push" |
|  | alias ast\_C101="ast\_new;STATE=C101;ast\_push" |
|  | alias ast\_C102="ast\_new;STATE=C102;ast\_push" |
|  | alias ast\_C103="ast\_new;STATE=C103;ast\_push" |
|  | alias ast\_C104="ast\_new;STATE=C104;ast\_push" |
|  | alias ast\_C105="ast\_new;STATE=C105;ast\_push" |
|  | alias ast\_C106="ast\_new;STATE=C106;ast\_push" |
|  | alias ast\_C107="ast\_new;STATE=C107;ast\_push" |
|  | alias ast\_C108="ast\_new;STATE=C108;ast\_push" |
|  | alias ast\_C109="ast\_new;STATE=C109;ast\_push" |
|  | alias ast\_C110="ast\_new;STATE=C110;ast\_push" |
|  | alias ast\_C111="ast\_new;STATE=C111;ast\_push" |
|  | alias ast\_C112="ast\_new;STATE=C112;ast\_push" |
|  | alias ast\_C113="ast\_new;STATE=C113;ast\_push" |
|  | alias ast\_C114="ast\_new;STATE=C114;ast\_push" |
|  | alias ast\_C115="ast\_new;STATE=C115;ast\_push" |
|  | alias ast\_C116="ast\_new;STATE=C116;ast\_push" |
|  | alias ast\_C117="ast\_new;STATE=C117;ast\_push" |
|  | alias ast\_C118="ast\_new;STATE=C118;ast\_push" |
|  | alias ast\_C119="ast\_new;STATE=C119;ast\_push" |
|  | alias ast\_C120="ast\_new;STATE=C120;ast\_push" |
|  | alias ast\_C121="ast\_new;STATE=C121;ast\_push" |
|  | alias ast\_C122="ast\_new;STATE=C122;ast\_push" |
|  | alias ast\_C123="ast\_new;STATE=C123;ast\_push" |
|  | alias ast\_C124="ast\_new;STATE=C124;ast\_push" |
|  | alias ast\_C125="ast\_new;STATE=C125;ast\_push" |
|  | alias ast\_C126="ast\_new;STATE=C126;ast\_push" |
|  | alias ast\_C127="ast\_new;STATE=C127;ast\_push" |
|  | alias ast\_C128="ast\_new;STATE=C128;ast\_push" |
|  | alias ast\_C129="ast\_new;STATE=C129;ast\_push" |
|  | alias ast\_C130="ast\_new;STATE=C130;ast\_push" |
|  | alias ast\_C131="ast\_new;STATE=C131;ast\_push" |
|  | alias ast\_C132="ast\_new;STATE=C132;ast\_push" |
|  | alias ast\_C133="ast\_new;STATE=C133;ast\_push" |
|  | alias ast\_C134="ast\_new;STATE=C134;ast\_push" |
|  | alias ast\_C135="ast\_new;STATE=C135;ast\_push" |
|  | alias ast\_C136="ast\_new;STATE=C136;ast\_push" |
|  | alias ast\_C137="ast\_new;STATE=C137;ast\_push" |
|  | alias ast\_C138="ast\_new;STATE=C138;ast\_push" |
|  | alias ast\_C139="ast\_new;STATE=C139;ast\_push" |
|  | alias ast\_C140="ast\_new;STATE=C140;ast\_push" |
|  | alias ast\_C141="ast\_new;STATE=C141;ast\_push" |
|  | alias ast\_C142="ast\_new;STATE=C142;ast\_push" |
|  | alias ast\_C143="ast\_new;STATE=C143;ast\_push" |
|  | alias ast\_C144="ast\_new;STATE=C144;ast\_push" |
|  | alias ast\_C145="ast\_new;STATE=C145;ast\_push" |
|  | alias ast\_C146="ast\_new;STATE=C146;ast\_push" |
|  | alias ast\_C147="ast\_new;STATE=C147;ast\_push" |
|  | alias ast\_C148="ast\_new;STATE=C148;ast\_push" |
|  | alias ast\_C149="ast\_new;STATE=C149;ast\_push" |
|  | alias ast\_C150="ast\_new;STATE=C150;ast\_push" |
|  | alias ast\_C151="ast\_new;STATE=C151;ast\_push" |
|  | alias ast\_C152="ast\_new;STATE=C152;ast\_push" |
|  | alias ast\_C153="ast\_new;STATE=C153;ast\_push" |
|  | alias ast\_C154="ast\_new;STATE=C154;ast\_push" |
|  | alias ast\_C155="ast\_new;STATE=C155;ast\_push" |
|  | alias ast\_C156="ast\_new;STATE=C156;ast\_push" |
|  | alias ast\_C157="ast\_new;STATE=C157;ast\_push" |
|  | alias ast\_C158="ast\_new;STATE=C158;ast\_push" |
|  | alias ast\_C159="ast\_new;STATE=C159;ast\_push" |
|  | alias ast\_C160="ast\_new;STATE=C160;ast\_push" |
|  | alias ast\_C161="ast\_new;STATE=C161;ast\_push" |
|  | alias ast\_C162="ast\_new;STATE=C162;ast\_push" |
|  | alias ast\_C163="ast\_new;STATE=C163;ast\_push" |
|  | alias ast\_C164="ast\_new;STATE=C164;ast\_push" |
|  | alias ast\_C165="ast\_new;STATE=C165;ast\_push" |
|  | alias ast\_C166="ast\_new;STATE=C166;ast\_push" |
|  | alias ast\_C167="ast\_new;STATE=C167;ast\_push" |
|  | alias ast\_C168="ast\_new;STATE=C168;ast\_push" |
|  | alias ast\_C169="ast\_new;STATE=C169;ast\_push" |
|  | alias ast\_C170="ast\_new;STATE=C170;ast\_push" |
|  | alias ast\_C171="ast\_new;STATE=C171;ast\_push" |
|  | alias ast\_C172="ast\_new;STATE=C172;ast\_push" |
|  | alias ast\_C173="ast\_new;STATE=C173;ast\_push" |
|  | alias ast\_C174="ast\_new;STATE=C174;ast\_push" |
|  | alias ast\_C175="ast\_new;STATE=C175;ast\_push" |
|  | alias ast\_C176="ast\_new;STATE=C176;ast\_push" |
|  | alias ast\_C177="ast\_new;STATE=C177;ast\_push" |
|  | alias ast\_C178="ast\_new;STATE=C178;ast\_push" |
|  | alias ast\_C179="ast\_new;STATE=C179;ast\_push" |
|  | alias ast\_C180="ast\_new;STATE=C180;ast\_push" |
|  | alias ast\_C181="ast\_new;STATE=C181;ast\_push" |
|  | alias ast\_C182="ast\_new;STATE=C182;ast\_push" |
|  | alias ast\_C183="ast\_new;STATE=C183;ast\_push" |
|  | alias ast\_C184="ast\_new;STATE=C184;ast\_push" |
|  | alias ast\_C185="ast\_new;STATE=C185;ast\_push" |
|  | alias ast\_C186="ast\_new;STATE=C186;ast\_push" |
|  | alias ast\_C187="ast\_new;STATE=C187;ast\_push" |
|  | alias ast\_C188="ast\_new;STATE=C188;ast\_push" |
|  |  |
|  | # State codes: |
|  | # Ca=\_doc\_ Cb=file\_body Cc=item Cd=int\_item Ce=char\_item Cf=void\_item Cg=long\_item Ch=short\_item Ci=float\_item Cj=double\_item Ck=signed\_item Cl=unsigned\_item Cm=const\_item Cn=static\_item Co=extern\_item Cp=volatile\_item Cq=auto\_item Cr=register\_item Cs=typedef\_item Ct=struct\_item Cu=union\_item Cv=enum\_item Cw=decl\_rest Cx=ptr\_decl Cy=ident\_decl Cz=after\_name C1=func\_def C2=func\_end C3=func\_block C4=array\_decl C5=init\_part C6=more\_decls C7=declarator C8=param C9=param\_rest C10=param\_ptr C11=param\_type C12=param\_struct C13=param\_union C14=param\_enum C15=struct\_rest C16=enum\_rest C17=enum\_tail C18=enum\_vars C19=enumerator\_list C20=enumerator C21=initializer C22=brace\_init C23=return\_item C24=break\_item C25=continue\_item C26=goto\_item C27=if\_item C28=while\_item C29=for\_item C30=do\_item C31=switch\_item C32=case\_item C33=default\_item C34=sizeof\_item C35=pp\_line C36=block\_item C37=block\_body C38=expr\_item C39=expr C40=atom C41=sizeof\_expr C42=sizeof\_body C43=paren\_expr C44=arg\_list C45=str C46=chr C47=number C48=ident C49=\_unary\_1 C50=\_unary\_2 C51=\_unary\_3 C52=\_unary\_4 C53=\_unary\_5 C54=\_unary\_6 |
|  | # cont: C55 C56 C57 C58 C59 C60 C61 C62 C63 C64 C65 C66 C67 C68 C69 C70 C71 C72 C73 C74 C75 C76 C77 C78 C79 C80 C81 C82 C83 C84 C85 C86 C87 C88 C89 C90 C91 C92 C93 C94 C95 C96 C97 C98 C99 C100 C101 C102 C103 C104 C105 C106 C107 C108 C109 C110 C111 C112 C113 C114 C115 C116 C117 C118 C119 C120 C121 C122 C123 C124 C125 C126 C127 C128 C129 C130 C131 C132 C133 C134 C135 C136 C137 C138 C139 C140 C141 C142 C143 C144 C145 C146 C147 C148 C149 C150 C151 C152 C153 C154 C155 C156 C157 C158 C159 C160 C161 C162 C163 C164 C165 C166 C167 C168 C169 C170 C171 C172 C173 C174 C175 C176 C177 C178 C179 C180 C181 C182 C183 C184 C185 C186 C187 C188 |
|  | \_c89\_sg\_C45='[\\"]\*' |
|  | \_c89\_sg\_C46='[\\'"'"']\*' |
|  |  |
|  | \_EXP\_Ca='"\"" or '\'''\'''\'' or '\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''A'\'' or '\''R'\'' or '\''T'\'' or '\''B'\'' or '\''G'\'' or '\''#'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\''a'\'' or '\''r'\'' or '\''t'\'' or '\''b'\'' or '\''g'\'' or identifier or [0-9a-fA-FxXuUlL.] or text' |
|  | \_EXP\_Cb='"\"" or '\'''\'''\'' or '\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''A'\'' or '\''R'\'' or '\''T'\'' or '\''B'\'' or '\''G'\'' or '\''#'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\''a'\'' or '\''r'\'' or '\''t'\'' or '\''b'\'' or '\''g'\'' or identifier or [0-9a-fA-FxXuUlL.] or text' |
|  | \_EXP\_Cc='"\"" or '\'''\'''\'' or '\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''A'\'' or '\''R'\'' or '\''T'\'' or '\''B'\'' or '\''G'\'' or '\''#'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\''a'\'' or '\''r'\'' or '\''t'\'' or '\''b'\'' or '\''g'\'' or '\''w'\'' or identifier or [0-9a-fA-FxXuUlL.] or text' |
|  | \_EXP\_Cd=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Ce=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Cf=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Cg=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Ch=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Ci=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Cj=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Ck=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Cl=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Cm=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Cn=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Co=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Cp=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Cq=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Cr=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Cs=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Ct='identifier' |
|  | \_EXP\_Cu='identifier' |
|  | \_EXP\_Cv=''\''{'\'' or identifier' |
|  | \_EXP\_Cw=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Cx=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_Cy='identifier' |
|  | \_EXP\_Cz=''\''('\'' or '\'';'\'' or '\''['\'' or '\''='\'' or '\'','\''' |
|  | \_EXP\_C1=''\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\'')'\''' |
|  | \_EXP\_C2=''\''{'\'' or '\'';'\'' or '\'','\''' |
|  | \_EXP\_C3='"\"" or '\'''\'''\'' or '\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''A'\'' or '\''R'\'' or '\''T'\'' or '\''B'\'' or '\''G'\'' or '\''#'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\''a'\'' or '\''r'\'' or '\''t'\'' or '\''b'\'' or '\''g'\'' or '\''}'\'' or identifier or [0-9a-fA-FxXuUlL.] or text' |
|  | \_EXP\_C4='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or '\'']'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C5='"\"" or '\'''\'''\'' or '\''S'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C6=''\'';'\'' or '\'','\''' |
|  | \_EXP\_C7=''\''\*'\'' or identifier' |
|  | \_EXP\_C8=''\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\''' |
|  | \_EXP\_C9=''\''\*'\'' or identifier' |
|  | \_EXP\_C10=''\''\*'\'' or identifier' |
|  | \_EXP\_C11=''\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\''' |
|  | \_EXP\_C12='identifier' |
|  | \_EXP\_C13='identifier' |
|  | \_EXP\_C14='identifier' |
|  | \_EXP\_C15='identifier' |
|  | \_EXP\_C16='identifier' |
|  | \_EXP\_C17=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_C18=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_C19='identifier' |
|  | \_EXP\_C20='identifier' |
|  | \_EXP\_C21='"\"" or '\'''\'''\'' or '\''S'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C22='"\"" or '\'''\'''\'' or '\''S'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C23='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or '\'';'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C24=''\'';'\''' |
|  | \_EXP\_C25=''\'';'\''' |
|  | \_EXP\_C26='identifier' |
|  | \_EXP\_C27=''\''('\''' |
|  | \_EXP\_C28=''\''('\''' |
|  | \_EXP\_C29=''\''('\''' |
|  | \_EXP\_C30='"\"" or '\'''\'''\'' or '\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''A'\'' or '\''R'\'' or '\''T'\'' or '\''B'\'' or '\''G'\'' or '\''#'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\''a'\'' or '\''r'\'' or '\''t'\'' or '\''b'\'' or '\''g'\'' or identifier or [0-9a-fA-FxXuUlL.] or text' |
|  | \_EXP\_C31=''\''('\''' |
|  | \_EXP\_C32='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C33=''\'':'\''' |
|  | \_EXP\_C34=''\''('\''' |
|  | \_EXP\_C35='identifier' |
|  | \_EXP\_C36='"\"" or '\'''\'''\'' or '\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''A'\'' or '\''R'\'' or '\''T'\'' or '\''B'\'' or '\''G'\'' or '\''#'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\''a'\'' or '\''r'\'' or '\''t'\'' or '\''b'\'' or '\''g'\'' or '\''}'\'' or identifier or [0-9a-fA-FxXuUlL.] or text' |
|  | \_EXP\_C37='"\"" or '\'''\'''\'' or '\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''A'\'' or '\''R'\'' or '\''T'\'' or '\''B'\'' or '\''G'\'' or '\''#'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\''a'\'' or '\''r'\'' or '\''t'\'' or '\''b'\'' or '\''g'\'' or '\''}'\'' or identifier or [0-9a-fA-FxXuUlL.] or text' |
|  | \_EXP\_C38='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C39='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C40='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C41=''\''('\''' |
|  | \_EXP\_C42='identifier' |
|  | \_EXP\_C43='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C44='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C45='"\"" or '\''\'\''' |
|  | \_EXP\_C46=''\''\'\'' or '\'''\'''\''' |
|  | \_EXP\_C49='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C50='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C51='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C52='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C53='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C54='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C55='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C56='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\'')'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C57=''\'')'\''' |
|  | \_EXP\_C58='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\'']'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C59=''\'']'\''' |
|  | \_EXP\_C60='identifier' |
|  | \_EXP\_C61='identifier' |
|  | \_EXP\_C64='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C65=''\'':'\''' |
|  | \_EXP\_C66='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C67='"\"" or '\'''\'''\'' or '\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''A'\'' or '\''R'\'' or '\''T'\'' or '\''B'\'' or '\''G'\'' or '\''#'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\''a'\'' or '\''r'\'' or '\''t'\'' or '\''b'\'' or '\''g'\'' or identifier or [0-9a-fA-FxXuUlL.] or text' |
|  | \_EXP\_C90=''\''('\'' or '\'';'\'' or '\''['\'' or '\''='\'' or '\'','\''' |
|  | \_EXP\_C93=''\''{'\'' or '\'';'\'' or '\'','\''' |
|  | \_EXP\_C94=''\'','\''' |
|  | \_EXP\_C95=''\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\''' |
|  | \_EXP\_C99=''\'';'\'' or '\'','\''' |
|  | \_EXP\_C101=''\'';'\'' or '\'','\''' |
|  | \_EXP\_C103=''\''\*'\'' or identifier' |
|  | \_EXP\_C104=''\''['\'' or '\''='\''' |
|  | \_EXP\_C105='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or '\'']'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C106='"\"" or '\'''\'''\'' or '\''S'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C107=''\''\*'\'' or identifier' |
|  | \_EXP\_C115=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_C118=''\''{'\'' or '\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_C120=''\''}'\''' |
|  | \_EXP\_C121=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_C124=''\''}'\''' |
|  | \_EXP\_C125=''\''\*'\'' or '\'';'\'' or identifier' |
|  | \_EXP\_C127=''\'','\''' |
|  | \_EXP\_C128='identifier' |
|  | \_EXP\_C129=''\''='\''' |
|  | \_EXP\_C130='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C132=''\'','\'' or '\''}'\''' |
|  | \_EXP\_C133='"\"" or '\'''\'''\'' or '\''S'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C134=''\'';'\''' |
|  | \_EXP\_C135='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C136=''\'')'\''' |
|  | \_EXP\_C137='"\"" or '\'''\'''\'' or '\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''A'\'' or '\''R'\'' or '\''T'\'' or '\''B'\'' or '\''G'\'' or '\''#'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\''a'\'' or '\''r'\'' or '\''t'\'' or '\''b'\'' or '\''g'\'' or identifier or [0-9a-fA-FxXuUlL.] or text' |
|  | \_EXP\_C138=''\''E'\'' or '\''e'\''' |
|  | \_EXP\_C139='"\"" or '\'''\'''\'' or '\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''A'\'' or '\''R'\'' or '\''T'\'' or '\''B'\'' or '\''G'\'' or '\''#'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\''a'\'' or '\''r'\'' or '\''t'\'' or '\''b'\'' or '\''g'\'' or identifier or [0-9a-fA-FxXuUlL.] or text' |
|  | \_EXP\_C140='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C141=''\'')'\''' |
|  | \_EXP\_C142='"\"" or '\'''\'''\'' or '\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''A'\'' or '\''R'\'' or '\''T'\'' or '\''B'\'' or '\''G'\'' or '\''#'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\''a'\'' or '\''r'\'' or '\''t'\'' or '\''b'\'' or '\''g'\'' or identifier or [0-9a-fA-FxXuUlL.] or text' |
|  | \_EXP\_C144='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or '\'';'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C145='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or '\'';'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C146='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or '\'')'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C147='"\"" or '\'''\'''\'' or '\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''A'\'' or '\''R'\'' or '\''T'\'' or '\''B'\'' or '\''G'\'' or '\''#'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\''a'\'' or '\''r'\'' or '\''t'\'' or '\''b'\'' or '\''g'\'' or identifier or [0-9a-fA-FxXuUlL.] or text' |
|  | \_EXP\_C149=''\''w'\'' or '\''W'\''' |
|  | \_EXP\_C150=''\''('\''' |
|  | \_EXP\_C151='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C152=''\'')'\''' |
|  | \_EXP\_C153=''\'';'\''' |
|  | \_EXP\_C154='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C155=''\'')'\''' |
|  | \_EXP\_C156='"\"" or '\'''\'''\'' or '\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''A'\'' or '\''R'\'' or '\''T'\'' or '\''B'\'' or '\''G'\'' or '\''#'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\''a'\'' or '\''r'\'' or '\''t'\'' or '\''b'\'' or '\''g'\'' or identifier or [0-9a-fA-FxXuUlL.] or text' |
|  | \_EXP\_C158=''\'':'\''' |
|  | \_EXP\_C159='"\"" or '\'''\'''\'' or '\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''A'\'' or '\''R'\'' or '\''T'\'' or '\''B'\'' or '\''G'\'' or '\''#'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\''a'\'' or '\''r'\'' or '\''t'\'' or '\''b'\'' or '\''g'\'' or identifier or [0-9a-fA-FxXuUlL.] or text' |
|  | \_EXP\_C161='"\"" or '\'''\'''\'' or '\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''A'\'' or '\''R'\'' or '\''T'\'' or '\''B'\'' or '\''G'\'' or '\''#'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\''a'\'' or '\''r'\'' or '\''t'\'' or '\''b'\'' or '\''g'\'' or identifier or [0-9a-fA-FxXuUlL.] or text' |
|  | \_EXP\_C163='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  | \_EXP\_C164=''\'')'\''' |
|  | \_EXP\_C165=''\'';'\''' |
|  | \_EXP\_C169='"\"" or '\'''\'''\'' or '\''I'\'' or '\''C'\'' or '\''V'\'' or '\''L'\'' or '\''S'\'' or '\''F'\'' or '\''D'\'' or '\''U'\'' or '\''E'\'' or '\''A'\'' or '\''R'\'' or '\''T'\'' or '\''B'\'' or '\''G'\'' or '\''#'\'' or '\''{'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''i'\'' or '\''c'\'' or '\''v'\'' or '\''l'\'' or '\''s'\'' or '\''f'\'' or '\''d'\'' or '\''u'\'' or '\''e'\'' or '\''a'\'' or '\''r'\'' or '\''t'\'' or '\''b'\'' or '\''g'\'' or '\''}'\'' or identifier or [0-9a-fA-FxXuUlL.] or text' |
|  | \_EXP\_C171=''\'';'\''' |
|  | \_EXP\_C173='identifier' |
|  | \_EXP\_C174=''\'')'\''' |
|  | \_EXP\_C175=''\''\*'\'' or identifier' |
|  | \_EXP\_C176=''\'')'\''' |
|  | \_EXP\_C177=''\'','\''' |
|  | \_EXP\_C178='"\"" or '\'''\'''\'' or '\''S'\'' or '\''+'\'' or '\''&'\'' or '\''\*'\'' or '\''~'\'' or '\''!'\'' or '\''-'\'' or '\''('\'' or '\''s'\'' or identifier or [0-9a-fA-FxXuUlL.]' |
|  |  |
|  | # Steal last sibling from parent, make it first child of current NODE |
|  | alias \_steal='eval "\_W=\"\${X$PARN##\*\" \"}\" |
|  | X$PARN=\"\${X$PARN% \*}\" |
|  | X$NODE=\"\$X$NODE \$\_W\""' |
|  |  |
|  | \_c89\_parser\_prec () { |
|  | case "$1" in |
|  | '=') REPLY=1;; |
|  | '+=') REPLY=1;; |
|  | '-=') REPLY=1;; |
|  | '\*=') REPLY=1;; |
|  | '/=') REPLY=1;; |
|  | '%=') REPLY=1;; |
|  | '&=') REPLY=1;; |
|  | '|=') REPLY=1;; |
|  | '^=') REPLY=1;; |
|  | '<<=') REPLY=1;; |
|  | '>>=') REPLY=1;; |
|  | '||') REPLY=2;; |
|  | '&&') REPLY=3;; |
|  | '|') REPLY=4;; |
|  | '^') REPLY=5;; |
|  | '&') REPLY=6;; |
|  | '==') REPLY=7;; |
|  | '!=') REPLY=7;; |
|  | '<') REPLY=8;; |
|  | '>') REPLY=8;; |
|  | '<=') REPLY=8;; |
|  | '>=') REPLY=8;; |
|  | '<<') REPLY=9;; |
|  | '>>') REPLY=9;; |
|  | '+') REPLY=10;; |
|  | '-') REPLY=10;; |
|  | '\*') REPLY=11;; |
|  | '/') REPLY=11;; |
|  | '%') REPLY=11;; |
|  | '?') REPLY=0;; |
|  | '-') REPLY=12;; |
|  | '!') REPLY=12;; |
|  | '~') REPLY=12;; |
|  | '\*') REPLY=12;; |
|  | '&') REPLY=12;; |
|  | '++') REPLY=12;; |
|  | \*) REPLY=0;; |
|  | esac |
|  | } |
|  |  |
|  | c89\_parser () { |
|  | local CODE= STATE=Ca V=0 CONSUMED= STATES= NODES=" 0" X0="Ca" \ |
|  | NODE= PARN= PARNT= SIBL= REST= MATCH= \_a= \_W= \_ST= \_D= \_C= \_pq= \ |
|  | \_EOF=0 \_line= \_PREV= \_PLEN= \_PLC=0 \_JT=0 \ |
|  | \_XC=0 \_OP= \_np=0 \_cp=0 \ |
|  | \_CMT\_S='/\*' \_CMT\_SL=2 \_CMT\_E='\*/' \_CMT\_EL=2 \ |
|  | \_LN=1 \_COL=1 \_RD=0 |
|  |  |
|  | while :; do |
|  | pars\_progress |
|  | ast\_feed |
|  |  |
|  | # --- Expression completion (precedence climbing) --- |
|  | case $\_XC in 1) \_XC=0; case $STATE in C39|C55|C64|C66) |
|  | case "$CODE" in ' '\*|"$\_TAB"\*|"$\_EOL"\*) ast\_skip\_wse;; esac |
|  | case "$CODE" in |
|  | '-''>'\*) CODE="${CODE#"->"}"; \_COL=$((\_COL+2)); ast\_C61; \_steal; continue;; |
|  | '+''+'\*) CODE="${CODE#"++"}"; \_COL=$((\_COL+2)); ast\_C62; \_steal; ast\_close\_xc;; |
|  | '-''-'\*) CODE="${CODE#"--"}"; \_COL=$((\_COL+2)); ast\_C63; \_steal; ast\_close\_xc;; |
|  | '('\*) CODE="${CODE#"("}"; \_COL=$((\_COL+1)); ast\_C56; \_steal; continue;; |
|  | '['\*) CODE="${CODE#"["}"; \_COL=$((\_COL+1)); ast\_C58; \_steal; continue;; |
|  | '.'\*) CODE="${CODE#"."}"; \_COL=$((\_COL+1)); ast\_C60; \_steal; continue;; |
|  | esac |
|  | \_OP= |
|  | case "$CODE" in |
|  | '<''<''='\*) \_OP="<<="; \_np=1;; |
|  | '>''>''='\*) \_OP=">>="; \_np=1;; |
|  | '+''='\*) \_OP="+="; \_np=1;; |
|  | '-''='\*) \_OP="-="; \_np=1;; |
|  | '\*''='\*) \_OP="\*="; \_np=1;; |
|  | '/''='\*) \_OP="/="; \_np=1;; |
|  | '%''='\*) \_OP="%="; \_np=1;; |
|  | '&''='\*) \_OP="&="; \_np=1;; |
|  | '|''='\*) \_OP="|="; \_np=1;; |
|  | '^''='\*) \_OP="^="; \_np=1;; |
|  | '|''|'\*) \_OP="||"; \_np=2;; |
|  | '&''&'\*) \_OP="&&"; \_np=3;; |
|  | '=''='\*) \_OP="=="; \_np=7;; |
|  | '!''='\*) \_OP="!="; \_np=7;; |
|  | '<''='\*) \_OP="<="; \_np=8;; |
|  | '>''='\*) \_OP=">="; \_np=8;; |
|  | '<''<'\*) \_OP="<<"; \_np=9;; |
|  | '>''>'\*) \_OP=">>"; \_np=9;; |
|  | '='\*) \_OP="="; \_np=1;; |
|  | '|'\*) \_OP="|"; \_np=4;; |
|  | '^'\*) \_OP="^"; \_np=5;; |
|  | '&'\*) \_OP="&"; \_np=6;; |
|  | '<'\*) \_OP="<"; \_np=8;; |
|  | '>'\*) \_OP=">"; \_np=8;; |
|  | '+'\*) \_OP="+"; \_np=10;; |
|  | '-'\*) \_OP="-"; \_np=10;; |
|  | '\*'\*) \_OP="\*"; \_np=11;; |
|  | '/'\*) \_OP="/"; \_np=11;; |
|  | '%'\*) \_OP="%"; \_np=11;; |
|  | '?'\*) \_OP="?"; \_np=0;; |
|  | esac |
|  | case "$\_OP" in ?\*) |
|  | case $STATE in C55|C64|C66) |
|  | \_W="${NODES##\*" "}"; eval "\_W=\"\${V$\_W:-}\"" |
|  | \_c89\_parser\_prec "$\_W"; \_cp=$REPLY |
|  | case "$\_OP" in '='|'+='|'-='|'\*='|'/='|'%='|'&='|'|='|'^='|'<<='|'>>='|'?') case $((\_np < \_cp)) in 1) ast\_close\_xc;; esac;; |
|  | \*) case $((\_np <= \_cp)) in 1) ast\_close\_xc;; esac;; esac |
|  | ;; esac |
|  | ast\_consume\_op |
|  | case "$\_OP" in '?') ast\_C64; \_steal; continue;; esac |
|  | ast\_C55; \_steal; continue |
|  | ;; esac |
|  | case $STATE in C64) STATE=C65; continue;; esac |
|  | case $STATE in C66) ast\_close\_xc;; esac |
|  | case $STATE in C55) ast\_close\_xc;; esac |
|  | case $STATE in C39) ast\_close; \_PREV=; continue;; esac |
|  | ;; esac;; esac |
|  |  |
|  | # --- Fast paths (bulk accumulation) --- |
|  | case $STATE in |
|  | # str: accumulate (stops at close/esc) |
|  | C45) case $CODE in '"'\*|'\'\*|'') ;; \*) |
|  | ast\_more; REST="${CODE%%$\_c89\_sg\_C45}"; ast\_bulk\_nl;; esac;; |
|  | # chr: accumulate (stops at close/esc) |
|  | C46) case $CODE in "'"\*|'\'\*|'') ;; \*) |
|  | ast\_more; REST="${CODE%%$\_c89\_sg\_C46}"; ast\_bulk\_nl;; esac;; |
|  | # number: accumulate [0-9a-fA-FxXuUlL.] |
|  | C47) ast\_more; REST="${CODE%%[!0-9a-fA-FxXuUlL.]\*}" |
|  | case "$REST" in ?\*) ast\_bulk\_nl;; \*) ast\_close; \_XC=1; \_PREV=; continue;; esac;; |
|  | # ident: accumulate [a-zA-Z\_0-9] |
|  | C48) ast\_more; REST="${CODE%%[!a-zA-Z\_0-9]\*}" |
|  | case "$REST" in ?\*) ast\_bulk\_nl;; \*) ast\_close; \_XC=1; \_PREV=; continue;; esac;; |
|  | Cc|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|Cy|Cz|C1|C2|C3|C4|C5|C6|C7|C8|C9|C10|C11|C12|C13|C14|C15|C16|C17|C18|C19|C20|C21|C22|C23|C24|C25|C26|C27|C28|C29|C31|C32|C33|C34|C35|C36|C37|C38|C39|C40|C41|C42|C43|C44|C49|C50|C51|C52|C53|C54|C55|C56|C57|C58|C59|C60|C61|C62|C63|C64|C65|C66|C67|C90|C93|C94|C95|C99|C101|C103|C104|C105|C106|C107|C115|C118|C120|C121|C124|C125|C127|C128|C129|C130|C132|C133|C134|C135|C136|C138|C140|C141|C142|C144|C145|C146|C147|C149|C150|C151|C152|C153|C154|C155|C156|C158|C159|C161|C163|C164|C165|C171|C173|C174|C175|C176|C177|C178) |
|  | case $CODE in ' '\*|"$\_TAB"\*|"$\_EOL"\*) |
|  | ast\_skip; continue;; esac;; |
|  | esac |
|  |  |
|  | # Block comment skip |
|  | case $CODE in '/\*'\*) |
|  | ast\_cmt\_block;; |
|  | esac |
|  |  |
|  | # --- Character dispatch --- |
|  | case $CODE in |
|  |  |
|  | '"'\*) |
|  | case $STATE in |
|  | C45) ast\_close; ast\_skip; continue;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) STATE=C68; ast\_C38; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C45; ast\_skip; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C90|Cz|C93|C2|C99|C101|C107|C115|C35|C42|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | '\'\*) |
|  | case $STATE in |
|  | C45) |
|  | case ${CODE#?} in |
|  | '"'\*|'\'\*|'/'\*|'b'\*|'f'\*|'n'\*|'r'\*|'t'\*) |
|  | ast\_consume2;; |
|  | 'u'\*) case $CODE in |
|  | '\u'[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]\*) |
|  | REST="${CODE#??????}"; \_ast\_xfer; \_COL=$((\_COL+6));; |
|  | \*) \_error UNICODE;; esac;; |
|  | \*) \_error ESCAPE;; |
|  | esac; continue;; |
|  | C46) ast\_consume2; continue;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'WHILE') STATE=C68; ast\_C28; ast\_skip\_match; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C68; continue;; |
|  | esac;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C67|C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cc|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C90|Cz|C93|C2|C3|C99|C101|C107|C115|C21|C142|C147|C156|C159|C161|C35|C36|C37|C40|C42|C49|C50|C51|C52|C53|C54|C185|C186|C187|C188|C94|C105) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | "'"\*) |
|  | case $STATE in |
|  | C46) ast\_close; ast\_skip; continue;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) STATE=C68; ast\_C38; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C46; ast\_skip; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C90|Cz|C93|C2|C99|C101|C107|C115|C35|C42|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'I'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'INT') STATE=C68; ast\_Cd; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'IF') STATE=C68; ast\_C27; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'INT') CONSUMED='int'; ast\_skip\_match |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'C'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'CHAR') STATE=C68; ast\_Ce; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'CONST') STATE=C68; ast\_Cm; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'CONTINUE') STATE=C68; ast\_C25; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'CASE') STATE=C68; ast\_C32; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'CHAR') CONSUMED='char'; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})) |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | 'CONST') CONSUMED='const'; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})) |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | \*) CONSUMED="$MATCH"; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})) |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'V'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'VOID') STATE=C68; ast\_Cf; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'VOLATILE') STATE=C68; ast\_Cp; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'VOID') CONSUMED='void'; ast\_skip\_match |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'L'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'LONG') STATE=C68; ast\_Cg; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'LONG') CONSUMED='long'; ast\_skip\_match |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'S'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'SHORT') STATE=C68; ast\_Ch; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'SIGNED') STATE=C68; ast\_Ck; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'STATIC') STATE=C68; ast\_Cn; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'STRUCT') STATE=C68; ast\_Ct; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'SWITCH') STATE=C68; ast\_C31; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'SIZEOF') STATE=C68; ast\_C34; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'SHORT') CONSUMED='short'; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})) |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | 'SIGNED') CONSUMED='signed'; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})) |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | 'STRUCT') STATE=C111; ast\_C12; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) CONSUMED="$MATCH"; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})) |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'SIZEOF') STATE=C172; ast\_C41; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C172; ast\_C48; continue;; |
|  | esac;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'F'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'FLOAT') STATE=C68; ast\_Ci; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'FOR') STATE=C68; ast\_C29; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'FLOAT') CONSUMED='float'; ast\_skip\_match |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'D'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'DOUBLE') STATE=C68; ast\_Cj; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'DO') STATE=C68; ast\_C30; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'DEFAULT') STATE=C68; ast\_C33; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'DOUBLE') CONSUMED='double'; ast\_skip\_match |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'U'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'UNSIGNED') STATE=C68; ast\_Cl; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'UNION') STATE=C68; ast\_Cu; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'UNSIGNED') CONSUMED='unsigned'; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})) |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | 'UNION') STATE=C111; ast\_C13; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) CONSUMED="$MATCH"; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})) |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'E'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'EXTERN') STATE=C68; ast\_Co; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'ENUM') STATE=C68; ast\_Cv; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'ENUM') STATE=C111; ast\_C14; ast\_skip\_match; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C138) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'ELSE') ast\_skip\_match; STATE=C139; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; continue;; |
|  | esac;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'A'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'AUTO') STATE=C68; ast\_Cq; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'R'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'REGISTER') STATE=C68; ast\_Cr; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'RETURN') STATE=C68; ast\_C23; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'T'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'TYPEDEF') STATE=C68; ast\_Cs; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'B'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'BREAK') STATE=C68; ast\_C24; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'G'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'GOTO') STATE=C68; ast\_C26; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | '#'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) STATE=C68; ast\_C35; ast\_skip; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C90|Cz|C93|C2|C99|C101|C107|C115|C21|C35|C40|C42|C49|C50|C51|C52|C53|C54|C185|C186|C187|C188|C94|C105) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | '{'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) STATE=C68; ast\_C36; ast\_skip; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | C93) STATE=C96; ast\_C2; continue;; |
|  | C2) STATE=C97; ast\_C3; ast\_skip; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C21) STATE=C131; ast\_C22; ast\_skip; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cw|Cx|C90|Cz|C99|C101|C107|C115|C35|C40|C42|C49|C50|C51|C52|C53|C54|C185|C186|C187|C188|C94|C105) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | '+'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) STATE=C68; ast\_C38; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C54; ast\_skip; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C90|Cz|C93|C2|C99|C101|C107|C115|C35|C42|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | '&'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) STATE=C68; ast\_C38; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C53; ast\_skip; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C90|Cz|C93|C2|C99|C101|C107|C115|C35|C42|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | '\*'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) STATE=C68; ast\_C38; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Cw) STATE=C88; ast\_Cx; ast\_skip; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) ast\_skip; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C10; ast\_skip; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C17) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cx; ast\_skip; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C52; ast\_skip; continue;; |
|  | C175) ast\_skip; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|Ct|Cu|Cv|C90|Cz|C93|C2|C99|C101|C35|C42|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | '~'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) STATE=C68; ast\_C38; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C51; ast\_skip; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C90|Cz|C93|C2|C99|C101|C107|C115|C35|C42|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | '!'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) STATE=C68; ast\_C38; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C50; ast\_skip; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C90|Cz|C93|C2|C99|C101|C107|C115|C35|C42|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | '-'\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) STATE=C68; ast\_C38; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C49; ast\_skip; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C90|Cz|C93|C2|C99|C101|C107|C115|C35|C42|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | '('\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) STATE=C68; ast\_C38; continue;; |
|  | C90) STATE=C91; ast\_Cz; continue;; |
|  | Cz) STATE=C92; ast\_C1; ast\_skip; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C27) ast\_skip; STATE=C135; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C28) ast\_skip; STATE=C140; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C29) ast\_skip; STATE=C144; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C150) ast\_skip; STATE=C151; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C31) ast\_skip; STATE=C154; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C34) ast\_skip; STATE=C163; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C43; ast\_skip; continue;; |
|  | C41) ast\_skip; STATE=C173; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C93|C2|C99|C101|C107|C115|C35|C42|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'i'\*) |
|  | case $STATE in |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'INT') STATE=C68; ast\_Cd; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'IF') STATE=C68; ast\_C27; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'INT') CONSUMED='int'; ast\_skip\_match |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'c'\*) |
|  | case $STATE in |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'CHAR') STATE=C68; ast\_Ce; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'CONST') STATE=C68; ast\_Cm; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'CONTINUE') STATE=C68; ast\_C25; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'CASE') STATE=C68; ast\_C32; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'CHAR') CONSUMED='char'; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})) |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | 'CONST') CONSUMED='const'; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})) |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | \*) CONSUMED="$MATCH"; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})) |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'v'\*) |
|  | case $STATE in |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'VOID') STATE=C68; ast\_Cf; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'VOLATILE') STATE=C68; ast\_Cp; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'VOID') CONSUMED='void'; ast\_skip\_match |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'l'\*) |
|  | case $STATE in |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'LONG') STATE=C68; ast\_Cg; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'LONG') CONSUMED='long'; ast\_skip\_match |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 's'\*) |
|  | case $STATE in |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'SHORT') STATE=C68; ast\_Ch; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'SIGNED') STATE=C68; ast\_Ck; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'STATIC') STATE=C68; ast\_Cn; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'STRUCT') STATE=C68; ast\_Ct; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'SWITCH') STATE=C68; ast\_C31; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'SIZEOF') STATE=C68; ast\_C34; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'SHORT') CONSUMED='short'; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})) |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | 'SIGNED') CONSUMED='signed'; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})) |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | 'STRUCT') STATE=C111; ast\_C12; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) CONSUMED="$MATCH"; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})) |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | C40) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'SIZEOF') STATE=C172; ast\_C41; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C172; ast\_C48; continue;; |
|  | esac;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'f'\*) |
|  | case $STATE in |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'FLOAT') STATE=C68; ast\_Ci; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'FOR') STATE=C68; ast\_C29; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'FLOAT') CONSUMED='float'; ast\_skip\_match |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'd'\*) |
|  | case $STATE in |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'DOUBLE') STATE=C68; ast\_Cj; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'DO') STATE=C68; ast\_C30; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'DEFAULT') STATE=C68; ast\_C33; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'DOUBLE') CONSUMED='double'; ast\_skip\_match |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'u'\*) |
|  | case $STATE in |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'UNSIGNED') STATE=C68; ast\_Cl; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'UNION') STATE=C68; ast\_Cu; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'UNSIGNED') CONSUMED='unsigned'; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})) |
|  | ast\_C11; ast\_close; STATE=C111; continue;; |
|  | 'UNION') STATE=C111; ast\_C13; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) CONSUMED="$MATCH"; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})) |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'e'\*) |
|  | case $STATE in |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'EXTERN') STATE=C68; ast\_Co; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'ENUM') STATE=C68; ast\_Cv; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C11) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'ENUM') STATE=C111; ast\_C14; ast\_skip\_match; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C111; continue;; |
|  | esac;; |
|  | C138) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'ELSE') ast\_skip\_match; STATE=C139; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; continue;; |
|  | esac;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | C1) STATE=C94; ast\_C8; continue;; |
|  | C95) STATE=C94; ast\_C8; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C8) STATE=C107; ast\_C11; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C94) STATE=C94; ast\_C8; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'a'\*) |
|  | case $STATE in |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'AUTO') STATE=C68; ast\_Cq; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'r'\*) |
|  | case $STATE in |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'REGISTER') STATE=C68; ast\_Cr; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | 'RETURN') STATE=C68; ast\_C23; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 't'\*) |
|  | case $STATE in |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'TYPEDEF') STATE=C68; ast\_Cs; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'b'\*) |
|  | case $STATE in |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'BREAK') STATE=C68; ast\_C24; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'g'\*) |
|  | case $STATE in |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'GOTO') STATE=C68; ast\_C26; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'w'\*) |
|  | case $STATE in |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'WHILE') STATE=C68; ast\_C28; CODE="${CODE#"$MATCH"}"; \_COL=$((\_COL+${#MATCH})); continue;; |
|  | \*) STATE=C68; ast\_C38; continue;; |
|  | esac;; |
|  | C149) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'WHILE') ast\_skip\_match; STATE=C150; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; continue;; |
|  | esac;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | ';'\*) |
|  | case $STATE in |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Cw) ast\_Cw; ast\_skip; ast\_close; STATE=C88; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | C90) STATE=C91; ast\_Cz; continue;; |
|  | Cz) STATE=C92; ast\_C6; continue;; |
|  | C93) STATE=C96; ast\_C2; continue;; |
|  | C2) STATE=C97; ast\_C6; continue;; |
|  | C99) STATE=C100; ast\_C6; continue;; |
|  | C101) STATE=C102; ast\_C6; continue;; |
|  | C6) ast\_skip; ast\_close; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C17) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cw; ast\_skip; ast\_close; continue;; |
|  | C23) ast\_skip; ast\_close; continue;; |
|  | C24) ast\_skip; ast\_close; continue;; |
|  | C25) ast\_skip; ast\_close; continue;; |
|  | C134) ast\_skip; ast\_close; continue;; |
|  | C144) ast\_skip; STATE=C145; continue;; |
|  | C145) ast\_skip; STATE=C146; continue;; |
|  | C153) ast\_skip; ast\_close; continue;; |
|  | C165) ast\_skip; ast\_close; continue;; |
|  | C171) ast\_skip; ast\_close; continue;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'WHILE') STATE=C68; ast\_C28; ast\_skip\_match; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C68; continue;; |
|  | esac;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C67|C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cc|Ct|Cu|Cv|C3|C107|C21|C142|C147|C156|C159|C161|C35|C36|C37|C40|C42|C49|C50|C51|C52|C53|C54|C185|C186|C187|C188|C94|C105) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | '['\*) |
|  | case $STATE in |
|  | C90) STATE=C91; ast\_Cz; continue;; |
|  | Cz) STATE=C92; ast\_C4; ast\_skip; continue;; |
|  | C104) ast\_skip; STATE=C105; continue;; |
|  | C105) ast\_skip; STATE=C105; continue;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'WHILE') STATE=C68; ast\_C28; ast\_skip\_match; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C68; continue;; |
|  | esac;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C67|C68|C88|C91|C92|C97|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cc|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C93|C2|C3|C99|C101|C107|C115|C21|C142|C147|C156|C159|C161|C35|C36|C37|C40|C42|C49|C50|C51|C52|C53|C54|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | '='\*) |
|  | case $STATE in |
|  | C90) STATE=C91; ast\_Cz; continue;; |
|  | Cz) STATE=C92; ast\_C5; ast\_skip; continue;; |
|  | C104) ast\_skip; STATE=C106; continue;; |
|  | C129) ast\_skip; STATE=C130; continue;; |
|  | C105) ast\_skip; STATE=C106; continue;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'WHILE') STATE=C68; ast\_C28; ast\_skip\_match; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C68; continue;; |
|  | esac;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C67|C68|C88|C91|C92|C97|C108|C109|C111|C116|C117|C119|C123|C127|C131|C138|C168|C170|C172|C175|C177|Cc|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C93|C2|C3|C99|C101|C107|C115|C21|C142|C147|C156|C159|C161|C35|C36|C37|C40|C42|C49|C50|C51|C52|C53|C54|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | ','\*) |
|  | case $STATE in |
|  | C90) STATE=C91; ast\_Cz; continue;; |
|  | Cz) STATE=C92; ast\_C6; continue;; |
|  | C94) ast\_skip; STATE=C95; continue;; |
|  | C93) STATE=C96; ast\_C2; continue;; |
|  | C2) STATE=C97; ast\_C6; continue;; |
|  | C99) STATE=C100; ast\_C6; continue;; |
|  | C101) STATE=C102; ast\_C6; continue;; |
|  | C6) ast\_skip; STATE=C103; continue;; |
|  | C127) ast\_skip; STATE=C128; continue;; |
|  | C132) ast\_skip; STATE=C133; continue;; |
|  | C177) ast\_skip; STATE=C178; continue;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'WHILE') STATE=C68; ast\_C28; ast\_skip\_match; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C68; continue;; |
|  | esac;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C67|C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C129|C131|C138|C168|C170|C172|C175|Cc|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C3|C107|C115|C21|C142|C147|C156|C159|C161|C35|C36|C37|C40|C42|C49|C50|C51|C52|C53|C54|C185|C186|C187|C188|C105) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | ')'\*) |
|  | case $STATE in |
|  | C1) ast\_skip; STATE=C93; continue;; |
|  | C136) ast\_skip; STATE=C137; continue;; |
|  | C141) ast\_skip; STATE=C142; continue;; |
|  | C146) ast\_skip; STATE=C147; continue;; |
|  | C152) ast\_skip; STATE=C153; continue;; |
|  | C155) ast\_skip; STATE=C156; continue;; |
|  | C164) ast\_skip; STATE=C165; continue;; |
|  | C174) ast\_skip; ast\_close; continue;; |
|  | C176) ast\_skip; ast\_close; continue;; |
|  | C56) ast\_skip; ast\_close\_xc;; |
|  | C57) ast\_skip; ast\_close\_xc;; |
|  | C94) ast\_skip; STATE=C93; continue;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'WHILE') STATE=C68; ast\_C28; ast\_skip\_match; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C68; continue;; |
|  | esac;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C67|C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cc|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C90|Cz|C93|C2|C3|C99|C101|C107|C115|C21|C142|C147|C156|C159|C161|C35|C36|C37|C40|C42|C49|C50|C51|C52|C53|C54|C185|C186|C187|C188|C105) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | '}'\*) |
|  | case $STATE in |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C120) ast\_skip; STATE=C121; continue;; |
|  | C124) ast\_skip; STATE=C125; continue;; |
|  | C132) ast\_skip; ast\_close; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) ast\_C37; ast\_skip; ast\_close; STATE=C168; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'WHILE') STATE=C68; ast\_C28; ast\_skip\_match; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C68; continue;; |
|  | esac;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C67|C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cc|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C90|Cz|C93|C2|C99|C101|C107|C115|C21|C142|C147|C156|C159|C161|C35|C40|C42|C49|C50|C51|C52|C53|C54|C185|C186|C187|C188|C94|C105) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | ']'\*) |
|  | case $STATE in |
|  | C4) ast\_skip; STATE=C99; continue;; |
|  | C105) ast\_skip; STATE=C104; continue;; |
|  | C58) ast\_skip; ast\_close\_xc;; |
|  | C59) ast\_skip; ast\_close\_xc;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'WHILE') STATE=C68; ast\_C28; ast\_skip\_match; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C68; continue;; |
|  | esac;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C67|C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cc|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C90|Cz|C93|C2|C3|C99|C101|C107|C115|C21|C142|C147|C156|C159|C161|C35|C36|C37|C40|C42|C49|C50|C51|C52|C53|C54|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | 'W'\*) |
|  | case $STATE in |
|  | C149) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'WHILE') ast\_skip\_match; STATE=C150; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; continue;; |
|  | esac;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) STATE=C68; ast\_C38; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | ':'\*) |
|  | case $STATE in |
|  | C158) ast\_skip; STATE=C159; continue;; |
|  | C33) ast\_skip; STATE=C161; continue;; |
|  | C65) ast\_skip; STATE=C66; continue;; |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'WHILE') STATE=C68; ast\_C28; ast\_skip\_match; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C68; continue;; |
|  | esac;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C67|C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cc|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C90|Cz|C93|C2|C3|C99|C101|C107|C115|C21|C142|C147|C156|C159|C161|C35|C36|C37|C40|C42|C49|C50|C51|C52|C53|C54|C185|C186|C187|C188|C94|C105) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | [a-zA-Z\_0-90-9a-fA-FxXuUlL.]\*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) STATE=C68; ast\_C38; continue;; |
|  | Cd) STATE=C69; ast\_Cw; continue;; |
|  | Ce) STATE=C70; ast\_Cw; continue;; |
|  | Cf) STATE=C71; ast\_Cw; continue;; |
|  | Cg) STATE=C72; ast\_Cw; continue;; |
|  | Ch) STATE=C73; ast\_Cw; continue;; |
|  | Ci) STATE=C74; ast\_Cw; continue;; |
|  | Cj) STATE=C75; ast\_Cw; continue;; |
|  | Ck) STATE=C76; ast\_Cw; continue;; |
|  | Cl) STATE=C77; ast\_Cw; continue;; |
|  | Cm) STATE=C78; ast\_Cw; continue;; |
|  | Cn) STATE=C79; ast\_Cw; continue;; |
|  | Co) STATE=C80; ast\_Cw; continue;; |
|  | Cp) STATE=C81; ast\_Cw; continue;; |
|  | Cq) STATE=C82; ast\_Cw; continue;; |
|  | Cr) STATE=C83; ast\_Cw; continue;; |
|  | Cs) STATE=C84; ast\_Cw; continue;; |
|  | Ct) STATE=C85; ast\_C15; continue;; |
|  | Cu) STATE=C86; ast\_C15; continue;; |
|  | Cv) STATE=C87; ast\_C16; continue;; |
|  | Cw) STATE=C88; ast\_Cy; continue;; |
|  | Cx) STATE=C89; ast\_Cw; continue;; |
|  | Cy) STATE=C90; ast\_C48; continue;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C4) ast\_C39; continue;; |
|  | C5) STATE=C101; ast\_C21; continue;; |
|  | C103) STATE=C6; ast\_C7; continue;; |
|  | C7) STATE=C104; ast\_C48; continue;; |
|  | C105) ast\_C39; continue;; |
|  | C106) STATE=C104; ast\_C21; continue;; |
|  | C107) STATE=C108; ast\_C9; continue;; |
|  | C9) STATE=C109; ast\_C48; continue;; |
|  | C10) STATE=C110; ast\_C9; continue;; |
|  | C12) STATE=C112; ast\_C48; continue;; |
|  | C13) STATE=C113; ast\_C48; continue;; |
|  | C14) STATE=C114; ast\_C48; continue;; |
|  | C15) STATE=C115; ast\_C48; continue;; |
|  | C115) STATE=C116; ast\_Cw; continue;; |
|  | C16) STATE=C118; ast\_C48; continue;; |
|  | C118) STATE=C119; ast\_C17; continue;; |
|  | C121) STATE=C122; ast\_C18; continue;; |
|  | C17) STATE=C124; ast\_C19; continue;; |
|  | C125) STATE=C126; ast\_C18; continue;; |
|  | C18) ast\_Cy; continue;; |
|  | C19) STATE=C127; ast\_C20; continue;; |
|  | C128) STATE=C127; ast\_C20; continue;; |
|  | C20) STATE=C129; ast\_C48; continue;; |
|  | C130) STATE=C129; ast\_C39; continue;; |
|  | C21) STATE=C131; ast\_C39; continue;; |
|  | C22) STATE=C132; ast\_C21; continue;; |
|  | C133) STATE=C132; ast\_C21; continue;; |
|  | C23) ast\_C39; continue;; |
|  | C26) STATE=C134; ast\_C48; continue;; |
|  | C135) STATE=C136; ast\_C39; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C140) STATE=C141; ast\_C39; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C144) ast\_C39; continue;; |
|  | C145) ast\_C39; continue;; |
|  | C146) ast\_C39; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C151) STATE=C152; ast\_C39; continue;; |
|  | C154) STATE=C155; ast\_C39; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C32) STATE=C158; ast\_C39; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C163) STATE=C164; ast\_C39; continue;; |
|  | C35) STATE=C166; ast\_C48; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | C38) STATE=C171; ast\_C39; continue;; |
|  | C39) ast\_C40; continue;; |
|  | C40) STATE=C172; ast\_C48; continue;; |
|  | C173) STATE=C174; ast\_C42; continue;; |
|  | C42) STATE=C175; ast\_C48; continue;; |
|  | C175) ast\_C48; continue;; |
|  | C43) STATE=C176; ast\_C39; continue;; |
|  | C44) STATE=C177; ast\_C39; continue;; |
|  | C178) STATE=C177; ast\_C39; continue;; |
|  | C49) STATE=C179; ast\_C40; continue;; |
|  | C50) STATE=C180; ast\_C40; continue;; |
|  | C51) STATE=C181; ast\_C40; continue;; |
|  | C52) STATE=C182; ast\_C40; continue;; |
|  | C53) STATE=C183; ast\_C40; continue;; |
|  | C54) STATE=C184; ast\_C40; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C55) ast\_C40; continue;; |
|  | C56) STATE=C57; ast\_C44; continue;; |
|  | C58) STATE=C59; ast\_C39; continue;; |
|  | C60) STATE=C185; ast\_C48; continue;; |
|  | C61) STATE=C186; ast\_C48; continue;; |
|  | C64) ast\_C40; continue;; |
|  | C66) ast\_C40; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C177|C90|Cz|C93|C2|C99|C101|C185|C186|C187|C188|C94) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  |  |
|  | '') |
|  | case $STATE in |
|  | C67|C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cc|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C90|Cz|C93|C2|C3|C99|C101|C107|C115|C21|C142|C147|C156|C159|C161|C35|C36|C37|C40|C42|C49|C50|C51|C52|C53|C54|C185|C186|C187|C188|C94|C105) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | C55) ast\_close; continue;; |
|  | C39) ast\_close; continue;; |
|  | Ca) break;; |
|  | \*) \_pars\_err\_eof;; |
|  | esac;; |
|  |  |
|  | \*) |
|  | case $STATE in |
|  | Cb) STATE=C67; ast\_Cc; continue;; |
|  | C67) ast\_Cb; continue;; |
|  | Cc) |
|  | ast\_more; MATCH="${CODE%%[!a-zA-Z0-9\_]\*}" |
|  | \_ucase "$MATCH" |
|  | case "$REPLY" in |
|  | 'WHILE') STATE=C68; ast\_C28; ast\_skip\_match; continue;; |
|  | \*) ast\_consume\_match |
|  | ast\_C48; ast\_close; STATE=C68; continue;; |
|  | esac;; |
|  | C3) STATE=C98; ast\_C37; continue;; |
|  | C137) STATE=C138; ast\_Cc; continue;; |
|  | C139) STATE=C138; ast\_Cc; continue;; |
|  | C142) STATE=C143; ast\_Cc; continue;; |
|  | C147) STATE=C148; ast\_Cc; continue;; |
|  | C30) STATE=C149; ast\_Cc; continue;; |
|  | C156) STATE=C157; ast\_Cc; continue;; |
|  | C159) STATE=C160; ast\_Cc; continue;; |
|  | C161) STATE=C162; ast\_Cc; continue;; |
|  | C36) STATE=C167; ast\_C37; continue;; |
|  | C37) STATE=C169; ast\_Cc; continue;; |
|  | C169) STATE=C170; ast\_C37; continue;; |
|  | Ca) STATE=Ca; ast\_Cb; continue;; |
|  | C68|C88|C91|C92|C97|C104|C108|C109|C111|C116|C117|C119|C123|C127|C129|C131|C138|C168|C170|C172|C175|C177|Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs|Ct|Cu|Cv|Cw|Cx|C90|Cz|C93|C2|C99|C101|C107|C115|C21|C35|C40|C42|C49|C50|C51|C52|C53|C54|C185|C186|C187|C188|C94|C105) ast\_close\_col\_xc;; |
|  | C69|C70|C71|C72|C73|C74|C75|C76|C77|C78|C79|C80|C81|C82|C83|C84|C85|C86|C87|C89|C96|C98|C100|C102|C110|C112|C113|C114|C122|C126|C143|C148|C157|C160|C162|C166|C167|C179|C180|C181|C182|C183|C184) ast\_close\_xc;; |
|  | \*) \_pars\_err;; |
|  | esac;; |
|  | esac |
|  | done |
|  |  |
|  | ast\_out |
|  | } |
|  |  |
|  | # --- modules/c89/unast.sh --- |
|  |  |
|  |  |
|  | # --- Emitter (AST to source reconstruction) --- |
|  |  |
|  | \_c89\_unast\_emit () { |
|  | local \_n=$1 \_t \_v \_r \_ch |
|  | IFS=' '; eval "set -- \$X$\_n"; IFS='' |
|  | \_t=$1; shift |
|  | eval "\_v=\"\${V$\_n:-}\"" |
|  |  |
|  | case "$\_t" in |
|  | Ca) \_r= |
|  | for \_ch in "$@"; do |
|  | case "$\_r" in ?\*) \_r="$\_r$\_EOL";; esac |
|  | \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY" |
|  | done; REPLY="$\_r";; |
|  | Cb) \_c89\_unast\_emit "$1"; \_r="$REPLY" |
|  | shift 1 |
|  | \_si=1 |
|  | case $# in 0) ;; \*) \_c89\_unast\_emit "$1"; \_r="${\_r} $REPLY"; shift;; esac |
|  | REPLY="${\_r}";; |
|  | Cc) case $# in 0) REPLY="$\_v";; 1) \_c89\_unast\_emit "$1";; \*) \_r=; for \_ch in "$@"; do \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY"; done; REPLY="$\_r";; esac;; |
|  | Cd) \_c89\_unast\_emit "$1"; REPLY="int ${REPLY}";; |
|  | Ce) \_c89\_unast\_emit "$1"; REPLY="char ${REPLY}";; |
|  | Cf) \_c89\_unast\_emit "$1"; REPLY="void ${REPLY}";; |
|  | Cg) \_c89\_unast\_emit "$1"; REPLY="long ${REPLY}";; |
|  | Ch) \_c89\_unast\_emit "$1"; REPLY="short ${REPLY}";; |
|  | Ci) \_c89\_unast\_emit "$1"; REPLY="float ${REPLY}";; |
|  | Cj) \_c89\_unast\_emit "$1"; REPLY="double ${REPLY}";; |
|  | Ck) \_c89\_unast\_emit "$1"; REPLY="signed ${REPLY}";; |
|  | Cl) \_c89\_unast\_emit "$1"; REPLY="unsigned ${REPLY}";; |
|  | Cm) \_c89\_unast\_emit "$1"; REPLY="const ${REPLY}";; |
|  | Cn) \_c89\_unast\_emit "$1"; REPLY="static ${REPLY}";; |
|  | Co) \_c89\_unast\_emit "$1"; REPLY="extern ${REPLY}";; |
|  | Cp) \_c89\_unast\_emit "$1"; REPLY="volatile ${REPLY}";; |
|  | Cq) \_c89\_unast\_emit "$1"; REPLY="auto ${REPLY}";; |
|  | Cr) \_c89\_unast\_emit "$1"; REPLY="register ${REPLY}";; |
|  | Cs) \_c89\_unast\_emit "$1"; REPLY="typedef ${REPLY}";; |
|  | Ct) \_c89\_unast\_emit "$1"; REPLY="struct ${REPLY}";; |
|  | Cu) \_c89\_unast\_emit "$1"; REPLY="union ${REPLY}";; |
|  | Cv) \_c89\_unast\_emit "$1"; REPLY="enum ${REPLY}";; |
|  | Cw) case $# in 0) case "$\_v" in ?\*) REPLY="$\_v";; \*) REPLY=";";; esac;; 1) \_c89\_unast\_emit "$1";; \*) \_r=; for \_ch in "$@"; do \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY"; done; REPLY="$\_r";; esac;; |
|  | Cx) \_c89\_unast\_emit "$1"; REPLY="\*${REPLY}";; |
|  | Cy) \_c89\_unast\_emit "$1"; \_r="$REPLY" |
|  | \_c89\_unast\_emit "$2"; REPLY="${\_r} ${REPLY}";; |
|  | Cz) case $# in 0) case "$\_v" in ?\*) REPLY="$\_v";; \*) REPLY=";";; esac;; 1) \_c89\_unast\_emit "$1";; \*) \_r=; for \_ch in "$@"; do \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY"; done; REPLY="$\_r";; esac;; |
|  | C1) \_r="(" |
|  | while test $# -gt 1; do |
|  | case "$\_r" in "(") ;; \*) \_r="$\_r,";; esac |
|  | \_c89\_unast\_emit "$1"; \_r="$\_r$REPLY"; shift |
|  | done |
|  | \_r="$\_r)" |
|  | \_c89\_unast\_emit "$1"; REPLY="$\_r${REPLY}";; |
|  | C2) case $# in 0) REPLY="$\_v";; 1) \_c89\_unast\_emit "$1";; \*) \_r=; for \_ch in "$@"; do \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY"; done; REPLY="$\_r";; esac;; |
|  | C3) \_c89\_unast\_emit "$1"; REPLY="{${REPLY}";; |
|  | C4) \_r="[" |
|  | case $# in 0) ;; \*) \_c89\_unast\_emit "$1"; \_r="${\_r}$REPLY"; shift;; esac |
|  | \_si=1 |
|  | case $# in 0) ;; \*) \_c89\_unast\_emit "$1"; \_r="${\_r}]$REPLY"; shift;; esac |
|  | case $# in 0) ;; \*) \_c89\_unast\_emit "$1"; \_r="${\_r} $REPLY"; shift;; esac |
|  | REPLY="${\_r}";; |
|  | C5) \_c89\_unast\_emit "$1"; \_r="=$REPLY" |
|  | \_c89\_unast\_emit "$2"; REPLY="${\_r} ${REPLY}";; |
|  | C6) \_r="" |
|  | for \_ch in "$@"; do |
|  | case "$\_r" in "") ;; \*) \_r="$\_r,";; esac |
|  | \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY" |
|  | done; REPLY="$\_r;";; |
|  | C7) \_r="" |
|  | while test $# -gt 3; do |
|  | case "$\_r" in "") ;; \*) \_r="$\_r ";; esac |
|  | \_c89\_unast\_emit "$1"; \_r="$\_r$REPLY"; shift |
|  | done |
|  | \_c89\_unast\_emit "$1"; REPLY="$\_r${REPLY}";; |
|  | C8) \_c89\_unast\_emit "$1"; \_r="$REPLY" |
|  | \_c89\_unast\_emit "$2"; REPLY="${\_r} ${REPLY}";; |
|  | C9) case $# in 0) REPLY="$\_v";; 1) \_c89\_unast\_emit "$1";; \*) \_r=; for \_ch in "$@"; do \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY"; done; REPLY="$\_r";; esac;; |
|  | C10) \_c89\_unast\_emit "$1"; REPLY="\*${REPLY}";; |
|  | C11) case $# in 0) REPLY="$\_v";; 1) \_c89\_unast\_emit "$1";; \*) \_r=; for \_ch in "$@"; do \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY"; done; REPLY="$\_r";; esac;; |
|  | C12) \_c89\_unast\_emit "$1"; REPLY="struct ${REPLY}";; |
|  | C13) \_c89\_unast\_emit "$1"; REPLY="union ${REPLY}";; |
|  | C14) \_c89\_unast\_emit "$1"; REPLY="enum ${REPLY}";; |
|  | C15) \_c89\_unast\_emit "$1"; \_r="$REPLY" |
|  | \_c89\_unast\_emit "$2"; REPLY="${\_r} ${REPLY}";; |
|  | C16) case $# in 0) REPLY="$\_v";; 1) \_c89\_unast\_emit "$1";; \*) \_r=; for \_ch in "$@"; do \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY"; done; REPLY="$\_r";; esac;; |
|  | C17) case $# in 0) REPLY="$\_v";; 1) \_c89\_unast\_emit "$1";; \*) \_r=; for \_ch in "$@"; do \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY"; done; REPLY="$\_r";; esac;; |
|  | C18) case $# in 0) REPLY="$\_v";; \*) \_c89\_unast\_emit "$1";; esac;; |
|  | C19) \_r="" |
|  | for \_ch in "$@"; do |
|  | case "$\_r" in "") ;; \*) \_r="$\_r,";; esac |
|  | \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY" |
|  | done; REPLY="$\_r";; |
|  | C20) \_c89\_unast\_emit "$1"; \_r="$REPLY" |
|  | shift 1 |
|  | \_si=1 |
|  | case $# in 0) ;; \*) \_c89\_unast\_emit "$1"; \_r="${\_r} = $REPLY"; shift;; esac |
|  | REPLY="${\_r}";; |
|  | C21) case $# in 0) REPLY="$\_v";; 1) \_c89\_unast\_emit "$1";; \*) \_r=; for \_ch in "$@"; do \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY"; done; REPLY="$\_r";; esac;; |
|  | C22) \_r="{" |
|  | for \_ch in "$@"; do |
|  | case "$\_r" in "{") ;; \*) \_r="$\_r,";; esac |
|  | \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY" |
|  | done; REPLY="$\_r,}";; |
|  | C23) case $# in 0) REPLY="return ;";; \*) \_c89\_unast\_emit "$1"; REPLY="return ${REPLY};";; esac;; |
|  | C24) REPLY="break;";; |
|  | C25) REPLY="continue;";; |
|  | C26) \_c89\_unast\_emit "$1"; REPLY="goto ${REPLY};";; |
|  | C27) \_c89\_unast\_emit "$1"; \_r="if($REPLY" |
|  | \_c89\_unast\_emit "$2"; \_r="${\_r})$REPLY" |
|  | shift 2 |
|  | \_si=2 |
|  | case $# in 0) ;; \*) \_c89\_unast\_emit "$1"; \_r="${\_r} else $REPLY"; shift;; esac |
|  | REPLY="${\_r}";; |
|  | C28) \_c89\_unast\_emit "$1"; \_r="while($REPLY" |
|  | \_c89\_unast\_emit "$2"; REPLY="${\_r})${REPLY}";; |
|  | C29) \_r="for(" |
|  | case $# in 0) ;; \*) \_c89\_unast\_emit "$1"; \_r="${\_r}$REPLY"; shift;; esac |
|  | \_si=1 |
|  | case $# in 0) ;; \*) \_c89\_unast\_emit "$1"; \_r="${\_r};$REPLY"; shift;; esac |
|  | case $# in 0) ;; \*) \_c89\_unast\_emit "$1"; \_r="${\_r};$REPLY"; shift;; esac |
|  | case $# in 0) ;; \*) \_c89\_unast\_emit "$1"; \_r="${\_r})$REPLY"; shift;; esac |
|  | case $# in 0) ;; \*) \_c89\_unast\_emit "$1"; \_r="${\_r} $REPLY"; shift;; esac |
|  | REPLY="${\_r}";; |
|  | C30) \_c89\_unast\_emit "$1"; \_r="do $REPLY" |
|  | \_c89\_unast\_emit "$2"; REPLY="${\_r} while(${REPLY});";; |
|  | C31) \_c89\_unast\_emit "$1"; \_r="switch($REPLY" |
|  | \_c89\_unast\_emit "$2"; REPLY="${\_r})${REPLY}";; |
|  | C32) \_c89\_unast\_emit "$1"; \_r="case $REPLY" |
|  | \_c89\_unast\_emit "$2"; REPLY="${\_r}: ${REPLY}";; |
|  | C33) \_c89\_unast\_emit "$1"; REPLY="default:${REPLY}";; |
|  | C34) \_c89\_unast\_emit "$1"; REPLY="sizeof(${REPLY});";; |
|  | C35) \_c89\_unast\_emit "$1"; REPLY="#${REPLY}";; |
|  | C36) \_c89\_unast\_emit "$1"; REPLY="{${REPLY}";; |
|  | C37) case $# in 0) case "$\_v" in ?\*) REPLY="$\_v";; \*) REPLY="}";; esac;; 1) \_c89\_unast\_emit "$1";; \*) \_r=; for \_ch in "$@"; do \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY"; done; REPLY="$\_r";; esac;; |
|  | C38) \_c89\_unast\_emit "$1"; REPLY="${REPLY};";; |
|  | C39) case $# in 0) REPLY="$\_v";; \*) \_c89\_unast\_emit "$1";; esac;; |
|  | C40) case $# in 0) REPLY="$\_v";; 1) \_c89\_unast\_emit "$1";; \*) \_r=; for \_ch in "$@"; do \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY"; done; REPLY="$\_r";; esac;; |
|  | C41) \_c89\_unast\_emit "$1"; REPLY="sizeof(${REPLY})";; |
|  | C42) \_r="" |
|  | for \_ch in "$@"; do |
|  | case "$\_r" in "") ;; \*) \_r="$\_r ";; esac |
|  | \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY" |
|  | done; REPLY="$\_r";; |
|  | C43) \_c89\_unast\_emit "$1"; REPLY="(${REPLY})";; |
|  | C44) \_r="" |
|  | for \_ch in "$@"; do |
|  | case "$\_r" in "") ;; \*) \_r="$\_r,";; esac |
|  | \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY" |
|  | done; REPLY="$\_r";; |
|  | C45) REPLY="\"$\_v\"";; |
|  | C46) REPLY="'$\_v'";; |
|  | C47) REPLY="$\_v";; |
|  | C48) REPLY="$\_v";; |
|  | C49) \_c89\_unast\_emit "$1"; REPLY="-${REPLY}";; |
|  | C50) \_c89\_unast\_emit "$1"; REPLY="!${REPLY}";; |
|  | C51) \_c89\_unast\_emit "$1"; REPLY="~${REPLY}";; |
|  | C52) \_c89\_unast\_emit "$1"; REPLY="\*${REPLY}";; |
|  | C53) \_c89\_unast\_emit "$1"; REPLY="&${REPLY}";; |
|  | C54) \_c89\_unast\_emit "$1"; REPLY="++${REPLY}";; |
|  | C55) \_c89\_unast\_emit "$1"; \_r="$REPLY" |
|  | \_c89\_unast\_emit "$2"; REPLY="$\_r$\_v$REPLY";; |
|  | C56) \_c89\_unast\_emit "$1"; \_r="$REPLY("; shift |
|  | local \_sep= |
|  | for \_ch in "$@"; do |
|  | case "$\_sep" in ?\*) \_r="$\_r, ";; esac |
|  | \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY"; \_sep=1 |
|  | done; REPLY="$\_r)";; |
|  | C58) \_c89\_unast\_emit "$1"; \_r="$REPLY["; shift |
|  | local \_sep= |
|  | for \_ch in "$@"; do |
|  | case "$\_sep" in ?\*) \_r="$\_r, ";; esac |
|  | \_c89\_unast\_emit "$\_ch"; \_r="$\_r$REPLY"; \_sep=1 |
|  | done; REPLY="$\_r]";; |
|  | C60) \_c89\_unast\_emit "$1"; \_r="$REPLY." |
|  | \_c89\_unast\_emit "$2"; REPLY="$\_r$REPLY";; |
|  | C61) \_c89\_unast\_emit "$1"; \_r="$REPLY->" |
|  | \_c89\_unast\_emit "$2"; REPLY="$\_r$REPLY";; |
|  | C62) \_c89\_unast\_emit "$1"; REPLY="$REPLY++";; |
|  | C63) \_c89\_unast\_emit "$1"; REPLY="$REPLY--";; |
|  | C64) \_c89\_unast\_emit "$1"; \_r="$REPLY?" |
|  | \_c89\_unast\_emit "$2"; \_r="$\_r$REPLY:" |
|  | \_c89\_unast\_emit "$3"; REPLY="$\_r$REPLY";; |
|  | \*) REPLY="??${\_t}??";; |
|  | esac |
|  | } |
|  |  |
|  | \_c89\_unast\_emit\_root () { \_c89\_unast\_emit "$@"; } |
|  |  |
|  | c89\_unast () { |
|  | \_readall; eval "$REPLY" |
|  | \_c89\_unast\_emit\_root 0 |
|  | \_printr1 "$REPLY" |
|  | } |
|  |  |
|  | # --- modules/tool/c89cc.sh --- |
|  | # ============================================================ |
|  | # C89 Compiler: AST → x86-64 ELF64 binary |
|  | # ============================================================ |
|  | # Usage: printf '%s' 'int main(){return 42;}' | sh gen/c89.sh | sh gen/c89cc.sh > a.out |
|  | # chmod +x a.out && ./a.out; echo $? |
|  | # |
|  | # Reads AST (V\*/X\* variable assignments) from stdin. |
|  | # Outputs a Linux x86-64 ELF64 executable to stdout. |
|  |  |
|  |  |
|  | # ============================================================ |
|  | # Pure-shell number/character conversion (no printf, no PATH) |
|  | # ============================================================ |
|  |  |
|  | # Decimal (0-255) → 2-char uppercase hex. Result in REPLY. |
|  | \_tool\_c89cc\_d2h () { |
|  | local \_hi=$(($1 / 16)) \_lo=$(($1 % 16)) \_hc \_lc |
|  | case $\_hi in 0) \_hc=0;; 1) \_hc=1;; 2) \_hc=2;; 3) \_hc=3;; |
|  | 4) \_hc=4;; 5) \_hc=5;; 6) \_hc=6;; 7) \_hc=7;; 8) \_hc=8;; |
|  | 9) \_hc=9;; 10) \_hc=A;; 11) \_hc=B;; 12) \_hc=C;; |
|  | 13) \_hc=D;; 14) \_hc=E;; 15) \_hc=F;; esac |
|  | case $\_lo in 0) \_lc=0;; 1) \_lc=1;; 2) \_lc=2;; 3) \_lc=3;; |
|  | 4) \_lc=4;; 5) \_lc=5;; 6) \_lc=6;; 7) \_lc=7;; 8) \_lc=8;; |
|  | 9) \_lc=9;; 10) \_lc=A;; 11) \_lc=B;; 12) \_lc=C;; |
|  | 13) \_lc=D;; 14) \_lc=E;; 15) \_lc=F;; esac |
|  | REPLY="$\_hc$\_lc" |
|  | } |
|  |  |
|  | # Character → decimal ASCII value. Result in REPLY. |
|  | \_tool\_c89cc\_c2d () { |
|  | case "$1" in |
|  | ' ') REPLY=32;; '!') REPLY=33;; '"') REPLY=34;; '#') REPLY=35;; |
|  | '$') REPLY=36;; '%') REPLY=37;; '&') REPLY=38;; "'") REPLY=39;; |
|  | '(') REPLY=40;; ')') REPLY=41;; '\*') REPLY=42;; '+') REPLY=43;; |
|  | ',') REPLY=44;; '-') REPLY=45;; '.') REPLY=46;; '/') REPLY=47;; |
|  | 0) REPLY=48;; 1) REPLY=49;; 2) REPLY=50;; 3) REPLY=51;; |
|  | 4) REPLY=52;; 5) REPLY=53;; 6) REPLY=54;; 7) REPLY=55;; |
|  | 8) REPLY=56;; 9) REPLY=57;; ':') REPLY=58;; ';') REPLY=59;; |
|  | '<') REPLY=60;; '=') REPLY=61;; '>') REPLY=62;; '?') REPLY=63;; |
|  | '@') REPLY=64;; |
|  | A) REPLY=65;; B) REPLY=66;; C) REPLY=67;; D) REPLY=68;; |
|  | E) REPLY=69;; F) REPLY=70;; G) REPLY=71;; H) REPLY=72;; |
|  | I) REPLY=73;; J) REPLY=74;; K) REPLY=75;; L) REPLY=76;; |
|  | M) REPLY=77;; N) REPLY=78;; O) REPLY=79;; P) REPLY=80;; |
|  | Q) REPLY=81;; R) REPLY=82;; S) REPLY=83;; T) REPLY=84;; |
|  | U) REPLY=85;; V) REPLY=86;; W) REPLY=87;; X) REPLY=88;; |
|  | Y) REPLY=89;; Z) REPLY=90;; '[') REPLY=91;; '\') REPLY=92;; |
|  | ']') REPLY=93;; '^') REPLY=94;; '\_') REPLY=95;; '`') REPLY=96;; |
|  | a) REPLY=97;; b) REPLY=98;; c) REPLY=99;; d) REPLY=100;; |
|  | e) REPLY=101;; f) REPLY=102;; g) REPLY=103;; h) REPLY=104;; |
|  | i) REPLY=105;; j) REPLY=106;; k) REPLY=107;; l) REPLY=108;; |
|  | m) REPLY=109;; n) REPLY=110;; o) REPLY=111;; p) REPLY=112;; |
|  | q) REPLY=113;; r) REPLY=114;; s) REPLY=115;; t) REPLY=116;; |
|  | u) REPLY=117;; v) REPLY=118;; w) REPLY=119;; x) REPLY=120;; |
|  | y) REPLY=121;; z) REPLY=122;; '{') REPLY=123;; '|') REPLY=124;; |
|  | '}') REPLY=125;; '~') REPLY=126;; \*) REPLY=63;; # unknown → '?' |
|  | esac |
|  | } |
|  |  |
|  | # Decimal → raw byte to stdout (uses fastest available output primitive) |
|  | if command -v printf >/dev/null 2>&1; then |
|  | \_out\_byte () { printf "\\$(($1/64))$((($1/8)%8))$(($1%8))"; } |
|  | elif command -v print >/dev/null 2>&1; then |
|  | \_out\_byte () { print -n "\\0$(($1/64))$((($1/8)%8))$(($1%8))"; } |
|  | else |
|  | \_out\_byte () { command -p printf "\\$(($1/64))$((($1/8)%8))$(($1%8))"; } |
|  | fi |
|  |  |
|  | # Emit a single hex byte from a decimal value |
|  | \_tool\_c89cc\_emit\_d () { \_tool\_c89cc\_d2h "$1"; \_tool\_c89cc\_emit "$REPLY"; } |
|  |  |
|  | # Emit a stack-offset from rbp. Uses 1-byte disp8 for off<=127, 4-byte disp32 otherwise. |
|  | # Caller must use the right opcode: 45/85 for mov, 45/85 for lea (ModRM byte differs). |
|  | # This function is called AFTER the opcode+ModRM byte is emitted. |
|  | \_tool\_c89cc\_emit\_off () { |
|  | if test $1 -le 127; then |
|  | \_tool\_c89cc\_d2h $(( 256 - $1 )) |
|  | \_tool\_c89cc\_emit "$REPLY" |
|  | else |
|  | \_tool\_c89cc\_emit\_le32 $(( 0 - $1 )) |
|  | fi |
|  | } |
|  |  |
|  | # Emit mov rax, [rbp-off] |
|  | \_tool\_c89cc\_load\_local () { |
|  | if test $1 -le 127; then \_tool\_c89cc\_emit "48 8B 45" |
|  | else \_tool\_c89cc\_emit "48 8B 85"; fi |
|  | \_tool\_c89cc\_emit\_off $1 |
|  | } |
|  | # Emit mov [rbp-off], rax |
|  | \_tool\_c89cc\_store\_local () { |
|  | if test $1 -le 127; then \_tool\_c89cc\_emit "48 89 45" |
|  | else \_tool\_c89cc\_emit "48 89 85"; fi |
|  | \_tool\_c89cc\_emit\_off $1 |
|  | } |
|  | # Emit lea rax, [rbp-off] |
|  | \_tool\_c89cc\_lea\_local () { |
|  | if test $1 -le 127; then \_tool\_c89cc\_emit "48 8D 45" |
|  | else \_tool\_c89cc\_emit "48 8D 85"; fi |
|  | \_tool\_c89cc\_emit\_off $1 |
|  | } |
|  |  |
|  | # ============================================================ |
|  | # Code Buffer |
|  | # ============================================================ |
|  | # Code is stored as per-byte variables: \_CB\_0, \_CB\_1, ... |
|  | # Each holds a 2-char hex string (e.g., "E8", "FF"). |
|  | # \_IP tracks the current offset (in bytes). |
|  | \_IP=0 |
|  |  |
|  | # Append hex bytes to the code buffer. Args: hex pairs (e.g., "48 89 E5") |
|  | \_tool\_c89cc\_emit () { |
|  | for \_b in $1; do |
|  | eval "\_CB\_$\_IP=\$\_b" |
|  | \_IP=$((\_IP + 1)) |
|  | done |
|  | } |
|  |  |
|  | # Read a byte from the code buffer at offset $1. Result in REPLY. |
|  | \_tool\_c89cc\_byte () { eval "REPLY=\$\_CB\_$1"; } |
|  |  |
|  | # Emit a 32-bit little-endian immediate value |
|  | \_tool\_c89cc\_emit\_le32 () { |
|  | local \_v=$1 |
|  | \_tool\_c89cc\_emit\_d $(( \_v & 255 )) |
|  | \_tool\_c89cc\_emit\_d $(( (\_v >> 8) & 255 )) |
|  | \_tool\_c89cc\_emit\_d $(( (\_v >> 16) & 255 )) |
|  | \_tool\_c89cc\_emit\_d $(( (\_v >> 24) & 255 )) |
|  | } |
|  |  |
|  | # Emit a 64-bit little-endian value |
|  | \_tool\_c89cc\_emit\_le64 () { |
|  | \_tool\_c89cc\_emit\_le32 "$1" |
|  | \_tool\_c89cc\_emit\_le32 0 |
|  | } |
|  |  |
|  | # ============================================================ |
|  | # Labels and Relocations |
|  | # ============================================================ |
|  | \_LABELS= # space-separated "name=offset" pairs |
|  | \_RELOCS= # space-separated "offset=name" pairs (rel32 fixups) |
|  | \_JMP\_N=0 # jump label counter |
|  | \_BRK\_LBL= # current break target label (loop/switch exit) |
|  | \_CONT\_LBL= # current continue target label (loop top) |
|  | \_SW\_OFF= # current switch value stack offset (for case comparisons) |
|  |  |
|  | \_tool\_c89cc\_label () { |
|  | \_LABELS="$\_LABELS $1=$\_IP" |
|  | } |
|  |  |
|  | # Emit a rel32 placeholder and record relocation |
|  | \_tool\_c89cc\_reloc\_rel32 () { |
|  | \_RELOCS="$\_RELOCS ${\_IP}=$1" |
|  | \_tool\_c89cc\_emit "00 00 00 00" # placeholder |
|  | } |
|  |  |
|  | # Allocate a jump label name. Returns name in REPLY. |
|  | \_tool\_c89cc\_jmp\_label () { |
|  | \_JMP\_N=$((\_JMP\_N + 1)) |
|  | REPLY=".LJ$\_JMP\_N" |
|  | } |
|  |  |
|  | # Emit a conditional jump (6 bytes: 0F 8x rel32) with auto-label. |
|  | # $1 = condition code (84=je, 85=jne, 8C=jl, 8F=jg, 8E=jle, 8D=jge) |
|  | # Returns: label name in REPLY (to be defined later at target) |
|  | \_tool\_c89cc\_emit\_jcc () { |
|  | \_tool\_c89cc\_jmp\_label |
|  | local \_jlbl=$REPLY |
|  | \_tool\_c89cc\_emit "0F $1" |
|  | \_RELOCS="$\_RELOCS J${\_IP}=$\_jlbl" |
|  | \_tool\_c89cc\_emit "00 00 00 00" |
|  | REPLY=$\_jlbl |
|  | } |
|  |  |
|  | # Emit an unconditional jump (5 bytes: E9 rel32) with auto-label. |
|  | \_tool\_c89cc\_emit\_jmp () { |
|  | \_tool\_c89cc\_jmp\_label |
|  | local \_jlbl=$REPLY |
|  | \_tool\_c89cc\_emit "E9" |
|  | \_RELOCS="$\_RELOCS J${\_IP}=$\_jlbl" |
|  | \_tool\_c89cc\_emit "00 00 00 00" |
|  | REPLY=$\_jlbl |
|  | } |
|  |  |
|  | # Define a jump label at current position |
|  | \_tool\_c89cc\_jmp\_target () { |
|  | \_tool\_c89cc\_label "$1" |
|  | } |
|  |  |
|  | # Resolve all relocations after code generation |
|  | \_tool\_c89cc\_fixup () { |
|  | # Calculate data section addresses for string/global fixups |
|  | local \_str\_base\_addr=$(( \_BASE\_ADDR + \_HDR\_SIZE + \_IP )) |
|  | local \_str\_size=$(( ${#\_STR\_DATA} / 2 )) |
|  | local \_glob\_base\_addr=$(( \_str\_base\_addr + \_str\_size )) |
|  |  |
|  | for \_rel in $\_RELOCS; do |
|  | local \_src="${\_rel%%=\*}" \_tgt\_name="${\_rel#\*=}" |
|  |  |
|  | # String address relocation: S<offset>=STR<id> |
|  | case "$\_src" in S\*) |
|  | local \_soff=${\_src#S} |
|  | local \_str\_id=${\_tgt\_name#STR} |
|  | eval "local \_sdataoff=\$\_STR\_OFF\_$\_str\_id" |
|  | # sdataoff is hex char offset, convert to byte offset |
|  | local \_sbyte=$(( \_sdataoff / 2 )) |
|  | local \_addr=$(( \_str\_base\_addr + \_sbyte )) |
|  | \_tool\_c89cc\_patch\_le64 $\_soff $\_addr |
|  | continue;; esac |
|  |  |
|  | # Global address relocation: G<offset>=GLOB<data\_off> |
|  | case "$\_src" in G\*) |
|  | local \_goff=${\_src#G} |
|  | local \_gdataoff=${\_tgt\_name#GLOB} |
|  | local \_addr=$(( \_glob\_base\_addr + \_gdataoff )) |
|  | \_tool\_c89cc\_patch\_le64 $\_goff $\_addr |
|  | continue;; esac |
|  |  |
|  | # Jump relocation: J<offset>=<label> |
|  | case "$\_src" in J\*) |
|  | local \_jsrc=${\_src#J} |
|  | local \_jtgt\_off= |
|  | for \_lbl in $\_LABELS; do |
|  | case "$\_lbl" in "${\_tgt\_name}="\*) |
|  | \_jtgt\_off="${\_lbl#\*=}"; break;; esac |
|  | done |
|  | case "$\_jtgt\_off" in ?\*) |
|  | local \_jdisp=$(( \_jtgt\_off - (\_jsrc + 4) )) |
|  | \_tool\_c89cc\_patch\_le32 $\_jsrc $\_jdisp;; esac |
|  | continue;; esac |
|  |  |
|  | # Regular rel32 relocation (call) |
|  | local \_tgt\_off= |
|  | for \_lbl in $\_LABELS; do |
|  | case "$\_lbl" in "${\_tgt\_name}="\*) |
|  | \_tgt\_off="${\_lbl#\*=}"; break;; esac |
|  | done |
|  | case "$\_tgt\_off" in '') continue;; esac |
|  | local \_disp=$(( \_tgt\_off - (\_src + 4) )) |
|  | \_tool\_c89cc\_patch\_le32 $\_src $\_disp |
|  | done |
|  | } |
|  |  |
|  | # Patch 8 bytes (64-bit address) at offset in code buffer |
|  | \_tool\_c89cc\_patch\_le64 () { |
|  | local \_off=$1 \_v=$2 \_i=0 |
|  | while test $\_i -lt 8; do |
|  | \_tool\_c89cc\_d2h $(( \_v % 256 )) |
|  | eval "\_CB\_$((\_off + \_i))=\$REPLY" |
|  | \_v=$(( \_v / 256 )) |
|  | \_i=$((\_i + 1)) |
|  | done |
|  | } |
|  |  |
|  | # Patch 4 bytes at offset in code buffer |
|  | \_tool\_c89cc\_patch\_le32 () { |
|  | local \_off=$1 \_v=$2 |
|  | \_tool\_c89cc\_d2h $(( \_v & 255 )); eval "\_CB\_$\_off=\$REPLY" |
|  | \_tool\_c89cc\_d2h $(( (\_v >> 8) & 255 )); eval "\_CB\_$((\_off+1))=\$REPLY" |
|  | \_tool\_c89cc\_d2h $(( (\_v >> 16) & 255 )); eval "\_CB\_$((\_off+2))=\$REPLY" |
|  | \_tool\_c89cc\_d2h $(( (\_v >> 24) & 255 )); eval "\_CB\_$((\_off+3))=\$REPLY" |
|  | } |
|  |  |
|  | # ============================================================ |
|  | # Symbol Table |
|  | # ============================================================ |
|  | \_SYM\_N=0 # number of symbols |
|  | \_SCOPE=0 # current scope depth |
|  | \_FRAME\_SIZE=0 # current function's stack frame size |
|  |  |
|  | # Add a symbol: name, kind, offset, elem\_size (for pointer subscript scale) |
|  | \_tool\_c89cc\_sym\_add () { |
|  | \_SYM\_N=$((\_SYM\_N + 1)) |
|  | eval "\_SYM\_NAME\_$\_SYM\_N=\"\$1\"" |
|  | eval "\_SYM\_KIND\_$\_SYM\_N=\"\$2\"" # func, local, global, param |
|  | eval "\_SYM\_SCOPE\_$\_SYM\_N=$\_SCOPE" |
|  | eval "\_SYM\_OFF\_$\_SYM\_N=\$3" # stack offset or 0 |
|  | eval "\_SYM\_ESIZE\_$\_SYM\_N=\${4:-8}" # element size for subscript (default 8) |
|  | } |
|  |  |
|  | # Look up symbol by name (searches current scope outward) |
|  | # Returns: "kind offset esize" |
|  | \_tool\_c89cc\_sym\_find () { |
|  | local \_i=$\_SYM\_N \_n |
|  | while test $\_i -gt 0; do |
|  | eval "\_n=\"\$\_SYM\_NAME\_$\_i\"" |
|  | case "$\_n" in "$1") |
|  | eval "REPLY=\"\$\_SYM\_KIND\_$\_i \$\_SYM\_OFF\_$\_i \$\_SYM\_ESIZE\_$\_i\"" |
|  | return 0;; esac |
|  | \_i=$((\_i - 1)) |
|  | done |
|  | REPLY= |
|  | return 1 |
|  | } |
|  |  |
|  | # Allocate a local variable on the stack. Returns offset. |
|  | \_tool\_c89cc\_alloc\_local () { |
|  | \_FRAME\_SIZE=$((\_FRAME\_SIZE + 8)) |
|  | REPLY=$\_FRAME\_SIZE |
|  | } |
|  |  |
|  | # Resolve element size for a pointer expression node. |
|  | # Walks AST to find the base variable and returns its esize in REPLY. |
|  | # Used by the \* dereference handler to decide byte vs qword load. |
|  | \_tool\_c89cc\_resolve\_esize () { |
|  | local \_re\_n=$1 \_re\_t |
|  | \_tool\_c89cc\_type "$\_re\_n"; \_re\_t=$REPLY |
|  | case "$\_re\_t" in |
|  | C39) # expr — delegate to child |
|  | \_tool\_c89cc\_children "$\_re\_n" |
|  | \_tool\_c89cc\_resolve\_esize "$REPLY";; |
|  | C48) # ident — look up symbol esize |
|  | \_tool\_c89cc\_val "$\_re\_n" |
|  | case "$REPLY" in [a-zA-Z\_]\*) |
|  | if \_tool\_c89cc\_sym\_find "$REPLY"; then |
|  | local \_re\_rest="$REPLY" |
|  | \_re\_rest="${\_re\_rest#\* }"; \_re\_rest="${\_re\_rest#\* }" |
|  | REPLY="${\_re\_rest%% \*}"; return |
|  | fi;; esac |
|  | REPLY=8;; |
|  | C53) # unary & — esize of the operand variable |
|  | \_tool\_c89cc\_children "$\_re\_n" |
|  | \_tool\_c89cc\_resolve\_esize "$REPLY";; |
|  | C55) # binary op (e.g., ptr + n) — esize of LHS |
|  | \_tool\_c89cc\_children "$\_re\_n" |
|  | \_tool\_c89cc\_resolve\_esize "${REPLY%% \*}";; |
|  | C43) # paren\_expr — delegate to child |
|  | \_tool\_c89cc\_children "$\_re\_n" |
|  | \_tool\_c89cc\_resolve\_esize "$REPLY";; |
|  | C58) # subscript a[i] — esize of base variable's element type |
|  | \_tool\_c89cc\_children "$\_re\_n" |
|  | \_tool\_c89cc\_resolve\_esize "${REPLY%% \*}";; |
|  | \*) REPLY=8;; |
|  | esac |
|  | } |
|  |  |
|  | # ============================================================ |
|  | # Global Variables |
|  | # ============================================================ |
|  | \_GLOB\_N=0 # number of globals |
|  | \_GLOB\_DATA= # hex bytes for .data section |
|  |  |
|  | \_tool\_c89cc\_glob\_add () { |
|  | \_GLOB\_N=$((\_GLOB\_N + 1)) |
|  | eval "\_GLOB\_NAME\_$\_GLOB\_N=\"\$1\"" |
|  | eval "\_GLOB\_SIZE\_$\_GLOB\_N=\$2" |
|  | # Allocate in data section (offset from data start) |
|  | local \_doff=0 \_i=1 |
|  | while test $\_i -lt $\_GLOB\_N; do |
|  | eval "\_doff=\$((\_doff + \$\_GLOB\_SIZE\_$\_i))" |
|  | \_i=$((\_i + 1)) |
|  | done |
|  | eval "\_GLOB\_OFF\_$\_GLOB\_N=$\_doff" |
|  | \_tool\_c89cc\_sym\_add "$1" "global" "$\_doff" "${3:-8}" |
|  | # Zero-fill in data section |
|  | local \_j=0 |
|  | while test $\_j -lt $2; do \_GLOB\_DATA="${\_GLOB\_DATA}00"; \_j=$((\_j + 1)); done |
|  | } |
|  |  |
|  | # Look up global by name → offset in data section |
|  | \_tool\_c89cc\_glob\_find () { |
|  | local \_i=1 |
|  | while test $\_i -le $\_GLOB\_N; do |
|  | eval "case \"\$\_GLOB\_NAME\_$\_i\" in \"\$1\") eval \"REPLY=\\\$\_GLOB\_OFF\_$\_i\"; return 0;; esac" |
|  | \_i=$((\_i + 1)) |
|  | done |
|  | return 1 |
|  | } |
|  |  |
|  | # ============================================================ |
|  | # Struct Type Registry |
|  | # ============================================================ |
|  | \_STRUCT\_N=0 |
|  |  |
|  | # Register a struct: name, field\_count, field\_names, field\_sizes |
|  | \_tool\_c89cc\_struct\_def () { |
|  | \_STRUCT\_N=$((\_STRUCT\_N + 1)) |
|  | eval "\_STRUCT\_NAME\_$\_STRUCT\_N=\"\$1\"" |
|  | eval "\_STRUCT\_NFIELDS\_$\_STRUCT\_N=0" |
|  | } |
|  |  |
|  | # Add field to last defined struct |
|  | \_tool\_c89cc\_struct\_field () { |
|  | local \_si=$\_STRUCT\_N \_nf |
|  | eval "\_nf=\$\_STRUCT\_NFIELDS\_$\_si" |
|  | \_nf=$((\_nf + 1)) |
|  | eval "\_STRUCT\_NFIELDS\_$\_si=$\_nf" |
|  | eval "\_STRUCT\_FNAME\_${\_si}\_${\_nf}=\"\$1\"" |
|  | eval "\_STRUCT\_FSIZE\_${\_si}\_${\_nf}=\$2" |
|  | } |
|  |  |
|  | # Look up struct field offset by struct name + field name |
|  | \_tool\_c89cc\_struct\_field\_off () { |
|  | local \_sname=$1 \_fname=$2 \_i=1 |
|  | while test $\_i -le $\_STRUCT\_N; do |
|  | eval "local \_sn=\"\$\_STRUCT\_NAME\_$\_i\"" |
|  | case "$\_sn" in "$\_sname") |
|  | local \_j=1 \_off=0 \_nf |
|  | eval "\_nf=\$\_STRUCT\_NFIELDS\_$\_i" |
|  | while test $\_j -le $\_nf; do |
|  | eval "local \_fn=\"\$\_STRUCT\_FNAME\_${\_i}\_${\_j}\"" |
|  | case "$\_fn" in "$\_fname") REPLY=$\_off; return 0;; esac |
|  | eval "local \_fs=\$\_STRUCT\_FSIZE\_${\_i}\_${\_j}" |
|  | # Align to 8 bytes |
|  | \_off=$(( (\_off + \_fs + 7) & -8 )) |
|  | \_j=$((\_j + 1)) |
|  | done |
|  | REPLY=$\_off; return 1;; # field not found |
|  | esac |
|  | \_i=$((\_i + 1)) |
|  | done |
|  | return 1 |
|  | } |
|  |  |
|  | # ============================================================ |
|  | # String Literals |
|  | # ============================================================ |
|  | \_STR\_N=0 |
|  | \_STR\_DATA= |
|  |  |
|  | \_tool\_c89cc\_add\_string () { |
|  | \_STR\_N=$((\_STR\_N + 1)) |
|  | eval "\_STR\_OFF\_$\_STR\_N=${#\_STR\_DATA}" |
|  | # Convert string to hex bytes, add null terminator |
|  | local \_s="$1" \_c |
|  | while test ${#\_s} -gt 0; do |
|  | \_c="${\_s%"${\_s#?}"}"; \_s="${\_s#?}" |
|  | case "$\_c" in |
|  | '\') # escape sequence |
|  | \_c="${\_s%"${\_s#?}"}"; \_s="${\_s#?}" |
|  | case "$\_c" in |
|  | n) \_STR\_DATA="${\_STR\_DATA}0A";; |
|  | t) \_STR\_DATA="${\_STR\_DATA}09";; |
|  | r) \_STR\_DATA="${\_STR\_DATA}0D";; |
|  | 0) \_STR\_DATA="${\_STR\_DATA}00";; |
|  | '\') \_STR\_DATA="${\_STR\_DATA}5C";; |
|  | '"') \_STR\_DATA="${\_STR\_DATA}22";; |
|  | \*) \_tool\_c89cc\_c2d "$\_c"; \_tool\_c89cc\_d2h "$REPLY"; \_STR\_DATA="${\_STR\_DATA}$REPLY";; |
|  | esac;; |
|  | \*) \_tool\_c89cc\_c2d "$\_c"; \_tool\_c89cc\_d2h "$REPLY"; \_STR\_DATA="${\_STR\_DATA}$REPLY";; |
|  | esac |
|  | done |
|  | \_STR\_DATA="${\_STR\_DATA}00" # null terminator |
|  | REPLY=$\_STR\_N |
|  | } |
|  |  |
|  | # ============================================================ |
|  | # AST Walker |
|  | # ============================================================ |
|  |  |
|  | # Get node type code (first word of X<n>) |
|  | \_tool\_c89cc\_type () { eval "REPLY=\"\${X$1%% \*}\""; } |
|  |  |
|  | # Get node value |
|  | \_tool\_c89cc\_val () { eval "REPLY=\"\${V$1:-}\""; } |
|  |  |
|  | # Get node children (everything after type code) |
|  | \_tool\_c89cc\_children () { |
|  | eval "local \_x=\"\$X$1\"" |
|  | REPLY="${\_x#\* }" |
|  | case "$REPLY" in "$\_x") REPLY=;; esac # no children |
|  | } |
|  |  |
|  | # Main recursive AST walker |
|  | \_tool\_c89cc\_node () { |
|  | local \_n=$1 \_t \_v |
|  | \_tool\_c89cc\_type "$\_n"; \_t=$REPLY |
|  | \_tool\_c89cc\_val "$\_n"; \_v=$REPLY |
|  |  |
|  | case "$\_t" in |
|  | Ca) # Document root: process all children |
|  | \_tool\_c89cc\_children "$\_n"; local \_ca\_chs="$REPLY" |
|  | for \_ch in $\_ca\_chs; do \_tool\_c89cc\_node "$\_ch"; done;; |
|  |  |
|  | Cb) # file\_body: process children |
|  | \_tool\_c89cc\_children "$\_n"; local \_cb\_chs="$REPLY" |
|  | for \_ch in $\_cb\_chs; do \_tool\_c89cc\_node "$\_ch"; done;; |
|  |  |
|  | Cd|Ce|Cf|Cg|Ch|Ci|Cj|Ck|Cl|Cm|Cn|Co|Cp|Cq|Cr|Cs) # type\_item (int, char, void, ...) |
|  | \_tool\_c89cc\_children "$\_n"; local \_dt\_chs="$REPLY" |
|  | for \_ch in $\_dt\_chs; do \_tool\_c89cc\_decl "$\_t" "$\_ch"; done;; |
|  |  |
|  | Ct|Cu) # struct/union item |
|  | \_tool\_c89cc\_children "$\_n" |
|  | for \_ch in $REPLY; do \_tool\_c89cc\_decl "$\_t" "$\_ch"; done;; |
|  |  |
|  | C38) # expr\_item: compile expression, discard result |
|  | \_tool\_c89cc\_children "$\_n"; local \_ei\_chs="$REPLY" |
|  | for \_ch in $\_ei\_chs; do \_tool\_c89cc\_expr "$\_ch"; done;; |
|  |  |
|  | C23) # return\_item |
|  | \_tool\_c89cc\_children "$\_n" |
|  | case "$REPLY" in |
|  | ?\*) \_tool\_c89cc\_expr "$REPLY";; # return expr → result in rax |
|  | \*) ;; # bare return |
|  | esac |
|  | # Epilogue: leave + ret |
|  | \_tool\_c89cc\_emit "C9" # leave |
|  | \_tool\_c89cc\_emit "C3";; # ret |
|  |  |
|  | C24) # break\_item — jump to break label |
|  | case "$\_BRK\_LBL" in ?\*) |
|  | \_tool\_c89cc\_emit "E9" |
|  | \_RELOCS="$\_RELOCS J${\_IP}=$\_BRK\_LBL" |
|  | \_tool\_c89cc\_emit "00 00 00 00";; esac;; |
|  | C25) # continue\_item — jump to continue label |
|  | case "$\_CONT\_LBL" in ?\*) |
|  | \_tool\_c89cc\_emit "E9" |
|  | \_RELOCS="$\_RELOCS J${\_IP}=$\_CONT\_LBL" |
|  | \_tool\_c89cc\_emit "00 00 00 00";; esac;; |
|  |  |
|  | C27) # if\_item: if(expr) item [else item] |
|  | \_tool\_c89cc\_children "$\_n"; local \_if\_chs="$REPLY" |
|  | set -- $\_if\_chs |
|  | local \_if\_cond="$1" \_if\_then="$2" \_if\_else="${3:-}" |
|  | \_tool\_c89cc\_expr "$\_if\_cond" |
|  | \_tool\_c89cc\_emit "48 85 C0" # test rax, rax |
|  | \_tool\_c89cc\_emit\_jcc "84"; local \_else\_lbl=$REPLY # je else/end |
|  | \_tool\_c89cc\_node "$\_if\_then" |
|  | case "$\_if\_else" in ?\*) |
|  | \_tool\_c89cc\_emit\_jmp; local \_end\_lbl=$REPLY # jmp end |
|  | \_tool\_c89cc\_jmp\_target "$\_else\_lbl" |
|  | \_tool\_c89cc\_node "$\_if\_else" |
|  | \_tool\_c89cc\_jmp\_target "$\_end\_lbl";; |
|  | \*) |
|  | \_tool\_c89cc\_jmp\_target "$\_else\_lbl";; |
|  | esac;; |
|  |  |
|  | C28) # while\_item: while(expr) item |
|  | \_tool\_c89cc\_children "$\_n"; local \_wh\_chs="$REPLY" |
|  | set -- $\_wh\_chs |
|  | local \_wh\_cond="$1" \_wh\_body="$2" |
|  | local \_sav\_brk=$\_BRK\_LBL \_sav\_cont=$\_CONT\_LBL |
|  | \_tool\_c89cc\_jmp\_label; local \_wh\_top=$REPLY |
|  | \_tool\_c89cc\_jmp\_target "$\_wh\_top" |
|  | \_tool\_c89cc\_expr "$\_wh\_cond" |
|  | \_tool\_c89cc\_emit "48 85 C0" |
|  | \_tool\_c89cc\_emit\_jcc "84"; local \_wh\_exit=$REPLY |
|  | \_BRK\_LBL=$\_wh\_exit; \_CONT\_LBL=$\_wh\_top |
|  | \_tool\_c89cc\_node "$\_wh\_body" |
|  | # Jump back to top |
|  | \_tool\_c89cc\_emit "E9" |
|  | \_RELOCS="$\_RELOCS J${\_IP}=$\_wh\_top" |
|  | \_tool\_c89cc\_emit "00 00 00 00" |
|  | \_tool\_c89cc\_jmp\_target "$\_wh\_exit" |
|  | \_BRK\_LBL=$\_sav\_brk; \_CONT\_LBL=$\_sav\_cont;; |
|  |  |
|  | C29) # for\_item: for(init;cond;incr) item |
|  | \_tool\_c89cc\_children "$\_n"; local \_for\_chs="$REPLY" |
|  | set -- $\_for\_chs |
|  | local \_for\_body \_for\_init= \_for\_cond= \_for\_incr= |
|  | case $# in |
|  | 1) \_for\_body=$1;; |
|  | 2) \_for\_cond=$1; \_for\_body=$2;; |
|  | 3) \_for\_init=$1; \_for\_cond=$2; \_for\_body=$3;; |
|  | 4) \_for\_init=$1; \_for\_cond=$2; \_for\_incr=$3; \_for\_body=$4;; |
|  | esac |
|  | local \_sav\_brk=$\_BRK\_LBL \_sav\_cont=$\_CONT\_LBL |
|  | case "$\_for\_init" in ?\*) \_tool\_c89cc\_expr "$\_for\_init";; esac |
|  | \_tool\_c89cc\_jmp\_label; local \_for\_top=$REPLY |
|  | \_tool\_c89cc\_jmp\_target "$\_for\_top" |
|  | local \_for\_exit\_lbl= |
|  | case "$\_for\_cond" in ?\*) |
|  | \_tool\_c89cc\_expr "$\_for\_cond" |
|  | \_tool\_c89cc\_emit "48 85 C0" |
|  | \_tool\_c89cc\_emit\_jcc "84"; \_for\_exit\_lbl=$REPLY;; |
|  | esac |
|  | \_tool\_c89cc\_jmp\_label; local \_for\_cont=$REPLY |
|  | \_BRK\_LBL=${\_for\_exit\_lbl:-}; \_CONT\_LBL=$\_for\_cont |
|  | \_tool\_c89cc\_node "$\_for\_body" |
|  | \_tool\_c89cc\_jmp\_target "$\_for\_cont" |
|  | case "$\_for\_incr" in ?\*) \_tool\_c89cc\_expr "$\_for\_incr";; esac |
|  | # Jump back to top |
|  | \_tool\_c89cc\_emit "E9" |
|  | \_RELOCS="$\_RELOCS J${\_IP}=$\_for\_top" |
|  | \_tool\_c89cc\_emit "00 00 00 00" |
|  | case "$\_for\_exit\_lbl" in ?\*) \_tool\_c89cc\_jmp\_target "$\_for\_exit\_lbl";; esac |
|  | \_BRK\_LBL=$\_sav\_brk; \_CONT\_LBL=$\_sav\_cont;; |
|  |  |
|  | C30) # do\_item: do item while(expr) |
|  | \_tool\_c89cc\_children "$\_n"; local \_do\_chs="$REPLY" |
|  | set -- $\_do\_chs |
|  | local \_do\_body="$1" \_do\_cond="$2" |
|  | local \_sav\_brk=$\_BRK\_LBL \_sav\_cont=$\_CONT\_LBL |
|  | \_tool\_c89cc\_jmp\_label; local \_do\_top=$REPLY |
|  | \_tool\_c89cc\_jmp\_label; local \_do\_exit=$REPLY |
|  | \_BRK\_LBL=$\_do\_exit; \_CONT\_LBL=$\_do\_top |
|  | \_tool\_c89cc\_jmp\_target "$\_do\_top" |
|  | \_tool\_c89cc\_node "$\_do\_body" |
|  | \_tool\_c89cc\_expr "$\_do\_cond" |
|  | \_tool\_c89cc\_emit "48 85 C0" |
|  | \_tool\_c89cc\_emit "0F 85" |
|  | \_RELOCS="$\_RELOCS J${\_IP}=$\_do\_top" |
|  | \_tool\_c89cc\_emit "00 00 00 00" |
|  | \_tool\_c89cc\_jmp\_target "$\_do\_exit" |
|  | \_BRK\_LBL=$\_sav\_brk; \_CONT\_LBL=$\_sav\_cont;; |
|  |  |
|  | C31) # switch\_item: switch(expr) { cases } |
|  | \_tool\_c89cc\_children "$\_n"; local \_sw\_chs="$REPLY" |
|  | set -- $\_sw\_chs |
|  | local \_sw\_cond="$1" \_sw\_body="$2" |
|  | local \_sav\_brk=$\_BRK\_LBL \_sav\_sw=$\_SW\_OFF |
|  | # Compile condition, save result as a local |
|  | \_tool\_c89cc\_expr "$\_sw\_cond" |
|  | \_tool\_c89cc\_alloc\_local; local \_sw\_loc=$REPLY |
|  | \_SW\_OFF=$\_sw\_loc |
|  | \_tool\_c89cc\_store\_local $\_sw\_loc # mov [rbp-off], rax |
|  | # Set up break label |
|  | \_tool\_c89cc\_jmp\_label; local \_sw\_end=$REPLY |
|  | \_BRK\_LBL=$\_sw\_end |
|  | # Process switch body (case/default labels handled below) |
|  | \_tool\_c89cc\_node "$\_sw\_body" |
|  | \_tool\_c89cc\_jmp\_target "$\_sw\_end" |
|  | \_BRK\_LBL=$\_sav\_brk; \_SW\_OFF=$\_sav\_sw;; |
|  |  |
|  | C32) # case\_item: case <value>: <statements> |
|  | \_tool\_c89cc\_children "$\_n"; local \_cs\_chs="$REPLY" |
|  | set -- $\_cs\_chs |
|  | local \_cs\_val="$1"; shift |
|  | # Compare switch value with case value |
|  | \_tool\_c89cc\_load\_local $\_SW\_OFF # mov rax, [rbp-sw\_off] |
|  | \_tool\_c89cc\_emit "50" # push rax (save switch val) |
|  | \_tool\_c89cc\_expr "$\_cs\_val" # rax = case value |
|  | \_tool\_c89cc\_emit "48 89 C1" # mov rcx, rax |
|  | \_tool\_c89cc\_emit "58" # pop rax (switch val) |
|  | \_tool\_c89cc\_emit "48 39 C8" # cmp rax, rcx |
|  | \_tool\_c89cc\_emit\_jcc "85"; local \_cs\_skip=$REPLY # jne → skip |
|  | # Case body: compile remaining children |
|  | for \_ch in "$@"; do \_tool\_c89cc\_node "$\_ch"; done |
|  | \_tool\_c89cc\_jmp\_target "$\_cs\_skip";; |
|  |  |
|  | C33) # default\_item: default: <statements> |
|  | \_tool\_c89cc\_children "$\_n"; local \_df\_chs="$REPLY" |
|  | for \_ch in $\_df\_chs; do \_tool\_c89cc\_node "$\_ch"; done;; |
|  |  |
|  | C36) # block\_item: { block\_body } |
|  | \_tool\_c89cc\_children "$\_n"; local \_bi\_chs="$REPLY" |
|  | for \_ch in $\_bi\_chs; do \_tool\_c89cc\_node "$\_ch"; done;; |
|  |  |
|  | C37) # block\_body: process children |
|  | \_tool\_c89cc\_children "$\_n"; local \_bb\_chs="$REPLY" |
|  | for \_ch in $\_bb\_chs; do \_tool\_c89cc\_node "$\_ch"; done;; |
|  |  |
|  | \*) ;; # Unknown node type — skip |
|  | esac |
|  | } |
|  |  |
|  | # ============================================================ |
|  | # Declaration Handler |
|  | # ============================================================ |
|  | \_tool\_c89cc\_decl () { |
|  | local \_type\_code=$1 \_child=$2 \_t \_v |
|  | \_tool\_c89cc\_type "$\_child"; \_t=$REPLY |
|  | \_tool\_c89cc\_val "$\_child"; \_v=$REPLY |
|  | # Determine element size from type keyword |
|  | # char/char \* → esize=1 (byte element); char \*\* → esize=8 (pointer elements) |
|  | # Third arg ($3) overrides when passed from Cx recursion — skip recomputation |
|  | local \_decl\_esize=8 |
|  | case "${3+set}" in set) \_decl\_esize=$3;; \*) |
|  | case "$\_type\_code" in Ce) |
|  | \_decl\_esize=1 |
|  | case "$\_t" in Cx) |
|  | \_tool\_c89cc\_children "$\_child" |
|  | \_tool\_c89cc\_type "$REPLY" |
|  | case "$REPLY" in Cx) \_decl\_esize=8;; esac |
|  | ;; esac |
|  | ;; esac |
|  | ;; esac |
|  |  |
|  | case "$\_t" in |
|  | Cy) # ident\_decl: name + after\_name |
|  | \_tool\_c89cc\_children "$\_child" |
|  | local \_name\_node="${REPLY%% \*}" \_rest="${REPLY#\* }" |
|  | \_tool\_c89cc\_val "$\_name\_node"; local \_name=$REPLY |
|  |  |
|  | # Check what follows: func\_def or variable |
|  | case "$\_rest" in '') |
|  | # Simple declaration (no initializer, no function) |
|  | case "$\_SCOPE" in |
|  | 0) \_tool\_c89cc\_glob\_add "$\_name" 8 "$\_decl\_esize";; # global |
|  | \*) \_tool\_c89cc\_alloc\_local; \_tool\_c89cc\_sym\_add "$\_name" "local" "$REPLY" "$\_decl\_esize";; |
|  | esac;; |
|  | \*) |
|  | \_tool\_c89cc\_type "$\_rest"; local \_rest\_t=$REPLY |
|  | case "$\_rest\_t" in |
|  | C1) # func\_def |
|  | \_tool\_c89cc\_func "$\_name" "$\_rest";; |
|  | C5) # init\_part (= initializer) |
|  | case "$\_SCOPE" in |
|  | 0) # Global with initializer — TODO: static init |
|  | \_tool\_c89cc\_glob\_add "$\_name" 8 "$\_decl\_esize";; |
|  | \*) |
|  | \_tool\_c89cc\_alloc\_local |
|  | local \_off=$REPLY |
|  | \_tool\_c89cc\_sym\_add "$\_name" "local" "$\_off" "$\_decl\_esize" |
|  | # Compile initializer expression |
|  | \_tool\_c89cc\_children "$\_rest" |
|  | local \_init\_expr="${REPLY%% \*}" |
|  | \_tool\_c89cc\_expr "$\_init\_expr" |
|  | # Store rax to local |
|  | \_tool\_c89cc\_store\_local $\_off;; |
|  | esac;; |
|  | Cz) # after\_name: could be ; or array or init |
|  | case "$\_SCOPE" in |
|  | 0) \_tool\_c89cc\_glob\_add "$\_name" 8 "$\_decl\_esize";; |
|  | \*) \_tool\_c89cc\_alloc\_local; \_tool\_c89cc\_sym\_add "$\_name" "local" "$REPLY" "$\_decl\_esize";; |
|  | esac;; |
|  | \*) # Other (more\_decls, etc.) |
|  | case "$\_SCOPE" in |
|  | 0) \_tool\_c89cc\_glob\_add "$\_name" 8 "$\_decl\_esize";; |
|  | \*) \_tool\_c89cc\_alloc\_local; \_tool\_c89cc\_sym\_add "$\_name" "local" "$REPLY" "$\_decl\_esize";; |
|  | esac;; |
|  | esac;; |
|  | esac;; |
|  |  |
|  | Cw) # decl\_rest — delegate (pass esize through) |
|  | \_tool\_c89cc\_children "$\_child" |
|  | case "$REPLY" in ?\*) \_tool\_c89cc\_decl "$\_type\_code" "$REPLY" "$\_decl\_esize";; esac;; |
|  |  |
|  | Cx) # ptr\_decl — pointer type, delegate to inner (pass esize through) |
|  | \_tool\_c89cc\_children "$\_child" |
|  | case "$REPLY" in ?\*) \_tool\_c89cc\_decl "$\_type\_code" "$REPLY" "$\_decl\_esize";; esac;; |
|  |  |
|  | \*) ;; # skip unknown |
|  | esac |
|  | } |
|  |  |
|  | # Look up field offset by field name. |
|  | # Uses struct registry if available, falls back to sequential 8-byte offsets. |
|  | \_tool\_c89cc\_field\_off () { |
|  | local \_fname=$1 |
|  | # Check struct registry first |
|  | local \_si=1 |
|  | while test $\_si -le $\_STRUCT\_N; do |
|  | local \_j=1 \_off=0 \_nf |
|  | eval "\_nf=\$\_STRUCT\_NFIELDS\_$\_si" |
|  | while test $\_j -le $\_nf; do |
|  | eval "local \_fn=\"\$\_STRUCT\_FNAME\_${\_si}\_${\_j}\"" |
|  | case "$\_fn" in "$\_fname") REPLY=$\_off; return;; esac |
|  | eval "local \_fs=\$\_STRUCT\_FSIZE\_${\_si}\_${\_j}" |
|  | \_off=$(( (\_off + \_fs + 7) & -8 )) # align to 8 |
|  | \_j=$((\_j + 1)) |
|  | done |
|  | \_si=$((\_si + 1)) |
|  | done |
|  | # Fallback: assume sequential 8-byte fields |
|  | REPLY=0 |
|  | } |
|  |  |
|  | # Count pointer depth in a param AST node (number of \* levels) |
|  | \_tool\_c89cc\_ptr\_depth () { |
|  | local \_pdn=$1 \_depth=0 \_pdt |
|  | \_tool\_c89cc\_children "$\_pdn" |
|  | local \_pd\_chs="$REPLY" |
|  | for \_pdc in $\_pd\_chs; do |
|  | \_tool\_c89cc\_type "$\_pdc"; \_pdt=$REPLY |
|  | case "$\_pdt" in |
|  | C10) # param\_ptr: count this \* and recurse |
|  | \_tool\_c89cc\_ptr\_depth "$\_pdc" |
|  | \_depth=$((\_depth + 1 + REPLY)) |
|  | REPLY=$\_depth; return;; |
|  | C9) # param\_rest: recurse |
|  | \_tool\_c89cc\_ptr\_depth "$\_pdc" |
|  | \_depth=$((\_depth + REPLY)) |
|  | REPLY=$\_depth; return;; |
|  | esac |
|  | done |
|  | REPLY=$\_depth |
|  | } |
|  |  |
|  | # Extract parameter name from param AST node (walks into param\_ptr chains) |
|  | \_tool\_c89cc\_param\_name () { |
|  | local \_pn=$1 \_pt |
|  | \_tool\_c89cc\_children "$\_pn" |
|  | local \_pn\_chs="$REPLY" |
|  | REPLY= |
|  | for \_pc in $\_pn\_chs; do |
|  | \_tool\_c89cc\_type "$\_pc"; \_pt=$REPLY |
|  | case "$\_pt" in |
|  | C48) \_tool\_c89cc\_val "$\_pc"; return;; # direct ident |
|  | C10|C9) \_tool\_c89cc\_param\_name "$\_pc"; return;; # param\_ptr or param\_rest: recurse |
|  | esac |
|  | done |
|  | } |
|  |  |
|  | # ============================================================ |
|  | # Function Compiler |
|  | # ============================================================ |
|  | \_tool\_c89cc\_func () { |
|  | local \_name=$1 \_fdef\_node=$2 |
|  | local \_saved\_frame=$\_FRAME\_SIZE \_saved\_sym=$\_SYM\_N |
|  |  |
|  | # Check if this is a definition (has func\_block) or just a declaration |
|  | \_tool\_c89cc\_children "$\_fdef\_node" |
|  | local \_fd\_chs="$REPLY" \_params= \_body= |
|  | for \_ch in $\_fd\_chs; do |
|  | \_tool\_c89cc\_type "$\_ch" |
|  | case "$REPLY" in |
|  | C3) \_body=$\_ch;; # func\_block |
|  | C8) \_params="$\_params $\_ch";; # param |
|  | esac |
|  | done |
|  |  |
|  | # If no body, this is a forward declaration — skip codegen |
|  | case "$\_body" in '') return;; esac |
|  |  |
|  | \_tool\_c89cc\_label "$\_name" |
|  | \_FRAME\_SIZE=0 |
|  | \_SCOPE=$((\_SCOPE + 1)) |
|  |  |
|  | # Function prologue |
|  | \_tool\_c89cc\_emit "55" # push rbp |
|  | \_tool\_c89cc\_emit "48 89 E5" # mov rbp, rsp |
|  |  |
|  | # Reserve space for sub rsp — we'll patch this later |
|  | local \_sub\_rsp\_pos=$\_IP |
|  | \_tool\_c89cc\_emit "48 81 EC" # sub rsp, imm32 |
|  | \_tool\_c89cc\_emit "00 00 00 00" # placeholder (patched after body) |
|  |  |
|  | # Allocate params as locals (System V ABI: rdi, rsi, rdx, rcx, r8, r9) |
|  | local \_pi=0 |
|  | for \_p in $\_params; do |
|  | \_pi=$((\_pi + 1)) |
|  | # Get param name (may be nested inside param\_ptr chains) |
|  | \_tool\_c89cc\_param\_name "$\_p" |
|  | local \_pname=$REPLY |
|  | case "$\_pname" in '') \_pname="\_param\_$\_pi";; esac |
|  |  |
|  | # Detect param type and pointer depth for element size |
|  | local \_param\_esize=8 \_param\_ptrdepth=0 \_base\_type=int |
|  | \_tool\_c89cc\_children "$\_p" |
|  | local \_p\_chs="$REPLY" |
|  | for \_ptc in $\_p\_chs; do |
|  | \_tool\_c89cc\_type "$\_ptc" |
|  | case "$REPLY" in |
|  | C11) \_tool\_c89cc\_val "$\_ptc"; \_base\_type=$REPLY;; |
|  | esac |
|  | done |
|  | # Count pointer depth by walking param\_ptr chain |
|  | \_tool\_c89cc\_ptr\_depth "$\_p"; \_param\_ptrdepth=$REPLY |
|  | # char\* with 1 pointer → byte elements; everything else → 8 |
|  | case "$\_base\_type" in char) |
|  | case "$\_param\_ptrdepth" in 1) \_param\_esize=1;; esac;; esac |
|  |  |
|  | \_tool\_c89cc\_alloc\_local |
|  | \_tool\_c89cc\_sym\_add "$\_pname" "param" "$REPLY" "$\_param\_esize" |
|  | local \_off=$REPLY |
|  |  |
|  | # Copy register arg to stack (mod=01 for disp8, mod=10 for disp32) |
|  | if test $\_off -le 127; then |
|  | case $\_pi in |
|  | 1) \_tool\_c89cc\_emit "48 89 7D";; 2) \_tool\_c89cc\_emit "48 89 75";; |
|  | 3) \_tool\_c89cc\_emit "48 89 55";; 4) \_tool\_c89cc\_emit "48 89 4D";; |
|  | 5) \_tool\_c89cc\_emit "4C 89 45";; 6) \_tool\_c89cc\_emit "4C 89 4D";; |
|  | esac |
|  | else |
|  | case $\_pi in |
|  | 1) \_tool\_c89cc\_emit "48 89 BD";; 2) \_tool\_c89cc\_emit "48 89 B5";; |
|  | 3) \_tool\_c89cc\_emit "48 89 95";; 4) \_tool\_c89cc\_emit "48 89 8D";; |
|  | 5) \_tool\_c89cc\_emit "4C 89 85";; 6) \_tool\_c89cc\_emit "4C 89 8D";; |
|  | esac |
|  | fi |
|  | \_tool\_c89cc\_emit\_off $\_off |
|  | done |
|  |  |
|  | # Compile function body |
|  | case "$\_body" in ?\*) |
|  | \_tool\_c89cc\_children "$\_body"; local \_fb\_chs="$REPLY" |
|  | for \_ch in $\_fb\_chs; do \_tool\_c89cc\_node "$\_ch"; done;; |
|  | esac |
|  |  |
|  | # Default return (in case no explicit return) |
|  | \_tool\_c89cc\_emit "48 31 C0" # xor rax, rax (return 0) |
|  | \_tool\_c89cc\_emit "C9" # leave |
|  | \_tool\_c89cc\_emit "C3" # ret |
|  |  |
|  | # Patch sub rsp with actual frame size (align to 16) |
|  | local \_aligned=$(( (\_FRAME\_SIZE + 15) & -16 )) |
|  | \_tool\_c89cc\_patch\_le32 $((\_sub\_rsp\_pos + 3)) $\_aligned |
|  |  |
|  | # Restore scope |
|  | \_SCOPE=$((\_SCOPE - 1)) |
|  | \_SYM\_N=$\_saved\_sym |
|  | \_FRAME\_SIZE=$\_saved\_frame |
|  | } |
|  |  |
|  | # ============================================================ |
|  | # Lvalue Compiler (address of expression in %rax) |
|  | # ============================================================ |
|  | \_tool\_c89cc\_lvalue () { |
|  | local \_n=$1 \_t \_v |
|  | \_tool\_c89cc\_type "$\_n"; \_t=$REPLY |
|  | \_tool\_c89cc\_val "$\_n"; \_v=$REPLY |
|  |  |
|  | case "$\_t" in |
|  | C39) # expr: delegate |
|  | \_tool\_c89cc\_children "$\_n" |
|  | \_tool\_c89cc\_lvalue "$REPLY";; |
|  | C48) # ident: address of variable |
|  | case "$\_v" in |
|  | [0-9]\*) echo "ERROR: cannot take address of number" >&2;; |
|  | \*) |
|  | if \_tool\_c89cc\_sym\_find "$\_v"; then |
|  | local \_lv\_rest="$REPLY" |
|  | local \_kind="${\_lv\_rest%% \*}"; \_lv\_rest="${\_lv\_rest#\* }" |
|  | local \_off="${\_lv\_rest%% \*}" |
|  | case "$\_kind" in |
|  | global) |
|  | \_tool\_c89cc\_emit "48 B8" |
|  | \_RELOCS="$\_RELOCS G${\_IP}=GLOB${\_off}" |
|  | \_tool\_c89cc\_emit "00 00 00 00 00 00 00 00";; |
|  | \*) |
|  | \_tool\_c89cc\_lea\_local $\_off;; |
|  | esac |
|  | else |
|  | echo "ERROR: undefined variable for lvalue: $\_v" >&2 |
|  | fi;; |
|  | esac;; |
|  | C52) # \*expr: address is the pointer value itself |
|  | \_tool\_c89cc\_children "$\_n" |
|  | \_tool\_c89cc\_expr "$REPLY";; |
|  | C58) # a[i]: address = base + index \* elem\_size |
|  | \_tool\_c89cc\_children "$\_n" |
|  | local \_ab="${REPLY%% \*}" \_ai="${REPLY#\* }" |
|  | local \_lv\_esize=8 |
|  | \_tool\_c89cc\_val "$\_ab" |
|  | case "$REPLY" in [a-zA-Z\_]\*) |
|  | if \_tool\_c89cc\_sym\_find "$REPLY"; then |
|  | local \_le\_rest="$REPLY" |
|  | \_le\_rest="${\_le\_rest#\* }"; \_le\_rest="${\_le\_rest#\* }" |
|  | \_lv\_esize="${\_le\_rest%% \*}" |
|  | fi;; esac |
|  | \_tool\_c89cc\_expr "$\_ab" |
|  | \_tool\_c89cc\_emit "50" |
|  | \_tool\_c89cc\_expr "$\_ai" |
|  | case "$\_lv\_esize" in |
|  | 1) ;; |
|  | 2) \_tool\_c89cc\_emit "48 C1 E0 01";; |
|  | 4) \_tool\_c89cc\_emit "48 C1 E0 02";; |
|  | 8) \_tool\_c89cc\_emit "48 C1 E0 03";; |
|  | esac |
|  | \_tool\_c89cc\_emit "59" |
|  | \_tool\_c89cc\_emit "48 01 C8";; |
|  | C60) # s.field: address = &s + offset |
|  | \_tool\_c89cc\_children "$\_n" |
|  | local \_sb="${REPLY%% \*}" \_sf="${REPLY#\* }" |
|  | \_tool\_c89cc\_lvalue "$\_sb" |
|  | \_tool\_c89cc\_val "$\_sf"; local \_sfn=$REPLY |
|  | \_tool\_c89cc\_field\_off "$\_sfn" |
|  | case "$REPLY" in 0) ;; \*) |
|  | \_tool\_c89cc\_emit "48 05"; \_tool\_c89cc\_emit\_le32 $REPLY;; esac;; |
|  | C61) # p->field: address = \*p + offset |
|  | \_tool\_c89cc\_children "$\_n" |
|  | local \_pb="${REPLY%% \*}" \_pf="${REPLY#\* }" |
|  | \_tool\_c89cc\_expr "$\_pb" # rax = pointer value |
|  | \_tool\_c89cc\_val "$\_pf"; local \_pfn=$REPLY |
|  | \_tool\_c89cc\_field\_off "$\_pfn" |
|  | case "$REPLY" in 0) ;; \*) |
|  | \_tool\_c89cc\_emit "48 05"; \_tool\_c89cc\_emit\_le32 $REPLY;; esac;; |
|  | \*) echo "ERROR: not an lvalue (type=$\_t)" >&2;; |
|  | esac |
|  | } |
|  |  |
|  | # ============================================================ |
|  | # Expression Compiler (result in %rax) |
|  | # ============================================================ |
|  | \_tool\_c89cc\_expr () { |
|  | local \_n=$1 \_t \_v |
|  | \_tool\_c89cc\_type "$\_n"; \_t=$REPLY |
|  | \_tool\_c89cc\_val "$\_n"; \_v=$REPLY |
|  |  |
|  | case "$\_t" in |
|  | C39) # expr: delegate to child |
|  | \_tool\_c89cc\_children "$\_n" |
|  | \_tool\_c89cc\_expr "$REPLY";; |
|  |  |
|  | C48) # ident or number literal |
|  | case "$\_v" in |
|  | [0-9]\*) # Number literal |
|  | local \_num |
|  | case "$\_v" in |
|  | 0x\*|0X\*) \_num=$(( \_v ));; # hex |
|  | 0[0-7]\*) \_num=$(( \_v ));; # octal (shell handles) |
|  | \*) \_num=$\_v;; # decimal |
|  | esac |
|  | \_tool\_c89cc\_emit "48 C7 C0" # mov rax, imm32 |
|  | \_tool\_c89cc\_emit\_le32 $\_num |
|  | ;; |
|  | \*) # Variable reference — load from stack or global |
|  | if \_tool\_c89cc\_sym\_find "$\_v"; then |
|  | local \_vr\_rest="$REPLY" |
|  | local \_kind="${\_vr\_rest%% \*}"; \_vr\_rest="${\_vr\_rest#\* }" |
|  | local \_off="${\_vr\_rest%% \*}" |
|  | case "$\_kind" in |
|  | global) |
|  | \_tool\_c89cc\_emit "48 B8" |
|  | \_RELOCS="$\_RELOCS G${\_IP}=GLOB${\_off}" |
|  | \_tool\_c89cc\_emit "00 00 00 00 00 00 00 00" |
|  | \_tool\_c89cc\_emit "48 8B 00";; |
|  | \*) |
|  | \_tool\_c89cc\_load\_local $\_off;; |
|  | esac |
|  | else |
|  | echo "ERROR: undefined variable: $\_v" >&2 |
|  | fi;; |
|  | esac;; |
|  |  |
|  | C55) # binary operator (precedence climbing) |
|  | \_tool\_c89cc\_children "$\_n" |
|  | local \_lhs="${REPLY%% \*}" \_rhs="${REPLY#\* }" |
|  | # Compile left operand |
|  | \_tool\_c89cc\_expr "$\_lhs" |
|  | \_tool\_c89cc\_emit "50" # push rax (save left) |
|  | # Compile right operand |
|  | \_tool\_c89cc\_expr "$\_rhs" |
|  | \_tool\_c89cc\_emit "48 89 C1" # mov rcx, rax (right in rcx) |
|  | \_tool\_c89cc\_emit "58" # pop rax (left in rax) |
|  | # Apply operator |
|  | case "$\_v" in |
|  | '+') \_tool\_c89cc\_emit "48 01 C8";; # add rax, rcx |
|  | '-') \_tool\_c89cc\_emit "48 29 C8";; # sub rax, rcx |
|  | '\*') \_tool\_c89cc\_emit "48 0F AF C1";; # imul rax, rcx |
|  | '/') \_tool\_c89cc\_emit "48 99" # cqo (sign-extend rax → rdx:rax) |
|  | \_tool\_c89cc\_emit "48 F7 F9";; # idiv rcx |
|  | '%') \_tool\_c89cc\_emit "48 99" # cqo |
|  | \_tool\_c89cc\_emit "48 F7 F9" # idiv rcx |
|  | \_tool\_c89cc\_emit "48 89 D0";; # mov rax, rdx (remainder) |
|  | '&') \_tool\_c89cc\_emit "48 21 C8";; # and rax, rcx |
|  | '|') \_tool\_c89cc\_emit "48 09 C8";; # or rax, rcx |
|  | '^') \_tool\_c89cc\_emit "48 31 C8";; # xor rax, rcx |
|  | '<<') \_tool\_c89cc\_emit "48 D3 E0";; # shl rax, cl |
|  | '>>') \_tool\_c89cc\_emit "48 D3 E8";; # shr rax, cl |
|  | '==') \_tool\_c89cc\_emit "48 39 C8" # cmp rax, rcx |
|  | \_tool\_c89cc\_emit "0F 94 C0" # sete al |
|  | \_tool\_c89cc\_emit "48 0F B6 C0";; # movzx rax, al |
|  | '!=') \_tool\_c89cc\_emit "48 39 C8" |
|  | \_tool\_c89cc\_emit "0F 95 C0" # setne al |
|  | \_tool\_c89cc\_emit "48 0F B6 C0";; |
|  | '<') \_tool\_c89cc\_emit "48 39 C8" |
|  | \_tool\_c89cc\_emit "0F 9C C0" # setl al |
|  | \_tool\_c89cc\_emit "48 0F B6 C0";; |
|  | '>') \_tool\_c89cc\_emit "48 39 C8" |
|  | \_tool\_c89cc\_emit "0F 9F C0" # setg al |
|  | \_tool\_c89cc\_emit "48 0F B6 C0";; |
|  | '<=') \_tool\_c89cc\_emit "48 39 C8" |
|  | \_tool\_c89cc\_emit "0F 9E C0" # setle al |
|  | \_tool\_c89cc\_emit "48 0F B6 C0";; |
|  | '>=') \_tool\_c89cc\_emit "48 39 C8" |
|  | \_tool\_c89cc\_emit "0F 9D C0" # setge al |
|  | \_tool\_c89cc\_emit "48 0F B6 C0";; |
|  | '=') # Assignment: compute lvalue address, store rvalue |
|  | # rcx = right value. Now compute left address and store. |
|  | \_tool\_c89cc\_emit "51" # push rcx (save rvalue) |
|  | \_tool\_c89cc\_lvalue "$\_lhs" # rax = address of lvalue |
|  | \_tool\_c89cc\_emit "59" # pop rcx (restore rvalue) |
|  | # Byte store for \*ptr and ptr[i] when char; 8-byte for vars |
|  | \_tool\_c89cc\_resolve\_esize "$\_lhs"; local \_asgn\_esz=$REPLY |
|  | # But plain variables always get 8-byte store (stack slots are 8 bytes) |
|  | # Only use byte store when LHS is a deref (\*p) or subscript (a[i]) |
|  | local \_asgn\_inner=$\_lhs |
|  | \_tool\_c89cc\_type "$\_asgn\_inner" |
|  | case "$REPLY" in C39) \_tool\_c89cc\_children "$\_asgn\_inner"; \_asgn\_inner=$REPLY; \_tool\_c89cc\_type "$\_asgn\_inner";; esac |
|  | case "$REPLY" in |
|  | C52|C58) # deref or subscript: use resolved esize |
|  | case "$\_asgn\_esz" in |
|  | 1) \_tool\_c89cc\_emit "88 08";; # mov [rax], cl (byte store) |
|  | \*) \_tool\_c89cc\_emit "48 89 08";; # mov [rax], rcx (qword store) |
|  | esac;; |
|  | \*) \_tool\_c89cc\_emit "48 89 08";; # mov [rax], rcx (qword store) |
|  | esac |
|  | \_tool\_c89cc\_emit "48 89 C8";; # mov rax, rcx (returns value) |
|  | '+='|'-='|'\*='|'/='|'%='|'&='|'|='|'^='|'<<='|'>>=') |
|  | # Compound assignment: load current, apply op, store back |
|  | \_tool\_c89cc\_emit "51" # push rcx (save rvalue) |
|  | \_tool\_c89cc\_lvalue "$\_lhs" # rax = address of lvalue |
|  | \_tool\_c89cc\_emit "50" # push rax (save address) |
|  | \_tool\_c89cc\_emit "48 8B 00" # mov rax, [rax] (load current) |
|  | \_tool\_c89cc\_emit "5A" # pop rdx (address in rdx) |
|  | \_tool\_c89cc\_emit "59" # pop rcx (rvalue) |
|  | local \_base\_op="${\_v%=}" |
|  | case "$\_base\_op" in |
|  | '+') \_tool\_c89cc\_emit "48 01 C8";; |
|  | '-') \_tool\_c89cc\_emit "48 29 C8";; |
|  | '\*') \_tool\_c89cc\_emit "48 0F AF C1";; |
|  | '/') \_tool\_c89cc\_emit "48 99"; \_tool\_c89cc\_emit "48 F7 F9";; |
|  | '%') \_tool\_c89cc\_emit "48 99"; \_tool\_c89cc\_emit "48 F7 F9"; \_tool\_c89cc\_emit "48 89 D0";; |
|  | '&') \_tool\_c89cc\_emit "48 21 C8";; |
|  | '|') \_tool\_c89cc\_emit "48 09 C8";; |
|  | '^') \_tool\_c89cc\_emit "48 31 C8";; |
|  | '<<') \_tool\_c89cc\_emit "48 D3 E0";; |
|  | '>>') \_tool\_c89cc\_emit "48 D3 E8";; |
|  | esac |
|  | \_tool\_c89cc\_emit "48 89 02" # mov [rdx], rax (store result) |
|  | ;; |
|  | '&&') # Logical AND: short-circuit |
|  | # Left in rax. If 0, skip right. |
|  | \_tool\_c89cc\_emit "48 85 C0" # test rax, rax |
|  | \_tool\_c89cc\_emit "0F 84" # je <skip> |
|  | local \_and\_skip=$\_IP |
|  | \_tool\_c89cc\_emit "00 00 00 00" |
|  | \_tool\_c89cc\_expr "$\_rhs" # evaluate right |
|  | # Normalize to 0/1 |
|  | \_tool\_c89cc\_emit "48 85 C0" # test rax, rax |
|  | \_tool\_c89cc\_emit "0F 95 C0" # setne al |
|  | \_tool\_c89cc\_emit "48 0F B6 C0" # movzx rax, al |
|  | local \_and\_end=$\_IP |
|  | \_tool\_c89cc\_patch\_le32 $\_and\_skip $(( \_and\_end - (\_and\_skip + 4) )) |
|  | # If skipped, rax is 0 (left was 0). Result correct. |
|  | ;; |
|  | '||') # Logical OR: short-circuit |
|  | \_tool\_c89cc\_emit "48 85 C0" # test rax, rax |
|  | \_tool\_c89cc\_emit "0F 85" # jne <skip> |
|  | local \_or\_skip=$\_IP |
|  | \_tool\_c89cc\_emit "00 00 00 00" |
|  | \_tool\_c89cc\_expr "$\_rhs" # evaluate right |
|  | local \_or\_end=$\_IP |
|  | \_tool\_c89cc\_patch\_le32 $\_or\_skip $(( \_or\_end - (\_or\_skip + 4) )) |
|  | # Normalize to 0/1 |
|  | \_tool\_c89cc\_emit "48 85 C0" # test rax, rax |
|  | \_tool\_c89cc\_emit "0F 95 C0" # setne al |
|  | \_tool\_c89cc\_emit "48 0F B6 C0" # movzx rax, al |
|  | ;; |
|  | esac;; |
|  |  |
|  | C56) # Function call postfix: fn(args) |
|  | \_tool\_c89cc\_children "$\_n" |
|  | local \_fn\_node="${REPLY%% \*}" \_arg\_node="${REPLY#\* }" |
|  | case "$\_arg\_node" in "$REPLY") \_arg\_node=;; esac |
|  | \_tool\_c89cc\_val "$\_fn\_node"; local \_fn\_name=$REPLY |
|  |  |
|  | # Compile arguments and push them |
|  | local \_argc=0 \_argi=0 |
|  | case "$\_arg\_node" in ?\*) |
|  | \_tool\_c89cc\_children "$\_arg\_node"; local \_arg\_chs="$REPLY" |
|  | # Count and compile args (push in reverse for stack, but use regs) |
|  | for \_a in $\_arg\_chs; do \_argc=$((\_argc + 1)); done |
|  | # Compile each arg, push on stack |
|  | for \_a in $\_arg\_chs; do |
|  | \_tool\_c89cc\_expr "$\_a" |
|  | \_tool\_c89cc\_emit "50" # push rax |
|  | done;; |
|  | esac |
|  |  |
|  | # \_\_syscall intrinsic: syscall(nr, a1, a2, a3, a4, a5, a6) |
|  | # Uses: rax=nr, rdi=a1, rsi=a2, rdx=a3, r10=a4, r8=a5, r9=a6 |
|  | case "$\_fn\_name" in \_\_syscall) |
|  | \_argi=$\_argc |
|  | while test $\_argi -gt 0; do |
|  | case $\_argi in |
|  | 1) \_tool\_c89cc\_emit "58";; # pop rax (syscall number) |
|  | 2) \_tool\_c89cc\_emit "5F";; # pop rdi (arg1) |
|  | 3) \_tool\_c89cc\_emit "5E";; # pop rsi (arg2) |
|  | 4) \_tool\_c89cc\_emit "5A";; # pop rdx (arg3) |
|  | 5) \_tool\_c89cc\_emit "41 5A";; # pop r10 (arg4) |
|  | 6) \_tool\_c89cc\_emit "41 58";; # pop r8 (arg5) |
|  | 7) \_tool\_c89cc\_emit "41 59";; # pop r9 (arg6) |
|  | esac |
|  | \_argi=$((\_argi - 1)) |
|  | done |
|  | \_tool\_c89cc\_emit "0F 05";; # syscall; result in rax |
|  | \*) |
|  | # Pop args into registers (System V ABI order) |
|  | \_argi=$\_argc |
|  | while test $\_argi -gt 0; do |
|  | case $\_argi in |
|  | 1) \_tool\_c89cc\_emit "5F";; # pop rdi (1st arg) |
|  | 2) \_tool\_c89cc\_emit "5E";; # pop rsi (2nd arg) |
|  | 3) \_tool\_c89cc\_emit "5A";; # pop rdx (3rd arg) |
|  | 4) \_tool\_c89cc\_emit "59";; # pop rcx (4th arg) |
|  | 5) \_tool\_c89cc\_emit "41 58";; # pop r8 (5th arg) |
|  | 6) \_tool\_c89cc\_emit "41 59";; # pop r9 (6th arg) |
|  | \*) ;; # leave on stack for >6 args |
|  | esac |
|  | \_argi=$((\_argi - 1)) |
|  | done |
|  |  |
|  | # Call function |
|  | \_tool\_c89cc\_emit "E8" # call <rel32> |
|  | \_tool\_c89cc\_reloc\_rel32 "$\_fn\_name" |
|  | # Result is in rax |
|  | ;; esac |
|  | ;; |
|  |  |
|  | C49|C50|C51|C52|C53|C54) # unary operators |
|  | \_tool\_c89cc\_children "$\_n" |
|  | case "$\_t" in |
|  | C52) # unary \* (dereference): compute address, then load |
|  | local \_deref\_child="$REPLY" \_deref\_esz=8 |
|  | \_tool\_c89cc\_resolve\_esize "$\_deref\_child"; \_deref\_esz=$REPLY |
|  | \_tool\_c89cc\_expr "$\_deref\_child" |
|  | case "$\_deref\_esz" in |
|  | 1) \_tool\_c89cc\_emit "48 0F B6 00";; # movzx rax, byte [rax] |
|  | \*) \_tool\_c89cc\_emit "48 8B 00";; # mov rax, [rax] |
|  | esac;; |
|  | C53) # unary & (address-of): compute lvalue address |
|  | \_tool\_c89cc\_lvalue "$REPLY";; |
|  | \*) # other unary: compute value first |
|  | \_tool\_c89cc\_expr "$REPLY" |
|  | case "$\_t" in |
|  | C49) \_tool\_c89cc\_emit "48 F7 D8";; # neg rax (unary -) |
|  | C50) # Logical NOT |
|  | \_tool\_c89cc\_emit "48 85 C0" # test rax, rax |
|  | \_tool\_c89cc\_emit "0F 94 C0" # sete al |
|  | \_tool\_c89cc\_emit "48 0F B6 C0";; # movzx rax, al |
|  | C51) \_tool\_c89cc\_emit "48 F7 D0";; # not rax (bitwise ~) |
|  | C54) ;; # unary ++ (pre-increment) — TODO |
|  | esac;; |
|  | esac;; |
|  |  |
|  | C64) # Ternary operator: cond ? true\_expr : false\_expr |
|  | \_tool\_c89cc\_children "$\_n" |
|  | set -- $REPLY |
|  | local \_tc="$1" \_tt="$2" \_tf="$3" |
|  | \_tool\_c89cc\_expr "$\_tc" |
|  | \_tool\_c89cc\_emit "48 85 C0" # test rax, rax |
|  | \_tool\_c89cc\_emit\_jcc "84"; local \_tern\_f=$REPLY # je false\_branch |
|  | \_tool\_c89cc\_expr "$\_tt" |
|  | \_tool\_c89cc\_emit\_jmp; local \_tern\_e=$REPLY # jmp end |
|  | \_tool\_c89cc\_jmp\_target "$\_tern\_f" |
|  | \_tool\_c89cc\_expr "$\_tf" |
|  | \_tool\_c89cc\_jmp\_target "$\_tern\_e";; |
|  |  |
|  | C58) # Array subscript: a[i] → base + index \* elem\_size |
|  | \_tool\_c89cc\_children "$\_n" |
|  | local \_arr\_base="${REPLY%% \*}" \_arr\_idx="${REPLY#\* }" |
|  | # Determine element size from base variable type |
|  | local \_arr\_esize=8 |
|  | \_tool\_c89cc\_val "$\_arr\_base" |
|  | case "$REPLY" in [a-zA-Z\_]\*) |
|  | if \_tool\_c89cc\_sym\_find "$REPLY"; then |
|  | local \_ae\_rest="$REPLY" |
|  | \_ae\_rest="${\_ae\_rest#\* }"; \_ae\_rest="${\_ae\_rest#\* }" # skip kind, off |
|  | \_arr\_esize="${\_ae\_rest%% \*}" |
|  | fi;; esac |
|  | \_tool\_c89cc\_expr "$\_arr\_base" # base address in rax |
|  | \_tool\_c89cc\_emit "50" # push rax |
|  | \_tool\_c89cc\_expr "$\_arr\_idx" # index in rax |
|  | case "$\_arr\_esize" in |
|  | 1) ;; # no scaling for char |
|  | 2) \_tool\_c89cc\_emit "48 C1 E0 01";; # shl rax, 1 |
|  | 4) \_tool\_c89cc\_emit "48 C1 E0 02";; # shl rax, 2 |
|  | 8) \_tool\_c89cc\_emit "48 C1 E0 03";; # shl rax, 3 |
|  | \*) \_tool\_c89cc\_emit "48 6B C0"; \_tool\_c89cc\_emit\_d $\_arr\_esize;; # imul rax, imm8 |
|  | esac |
|  | \_tool\_c89cc\_emit "59" # pop rcx (base) |
|  | \_tool\_c89cc\_emit "48 01 C8" # add rax, rcx |
|  | # Load: byte for char, qword for others |
|  | case "$\_arr\_esize" in |
|  | 1) \_tool\_c89cc\_emit "48 0F B6 00";; # movzx rax, byte [rax] |
|  | \*) \_tool\_c89cc\_emit "48 8B 00";; # mov rax, [rax] |
|  | esac;; |
|  |  |
|  | C62) # Postfix ++ |
|  | \_tool\_c89cc\_children "$\_n" |
|  | \_tool\_c89cc\_lvalue "$REPLY" # rax = address |
|  | \_tool\_c89cc\_emit "48 8B 08" # mov rcx, [rax] (old value) |
|  | \_tool\_c89cc\_emit "50" # push rax (save address) |
|  | \_tool\_c89cc\_emit "48 8D 41 01" # lea rax, [rcx+1] |
|  | \_tool\_c89cc\_emit "5A" # pop rdx (address) |
|  | \_tool\_c89cc\_emit "48 89 02" # mov [rdx], rax (store incremented) |
|  | \_tool\_c89cc\_emit "48 89 C8";; # mov rax, rcx (return OLD value) |
|  |  |
|  | C63) # Postfix -- |
|  | \_tool\_c89cc\_children "$\_n" |
|  | \_tool\_c89cc\_lvalue "$REPLY" |
|  | \_tool\_c89cc\_emit "48 8B 08" # mov rcx, [rax] |
|  | \_tool\_c89cc\_emit "50" |
|  | \_tool\_c89cc\_emit "48 8D 41 FF" # lea rax, [rcx-1] |
|  | \_tool\_c89cc\_emit "5A" |
|  | \_tool\_c89cc\_emit "48 89 02" |
|  | \_tool\_c89cc\_emit "48 89 C8";; |
|  |  |
|  | C60) # Member access: s.field → base + offset |
|  | \_tool\_c89cc\_children "$\_n" |
|  | local \_dot\_base="${REPLY%% \*}" \_dot\_field="${REPLY#\* }" |
|  | \_tool\_c89cc\_lvalue "$\_dot\_base" # rax = address of struct |
|  | \_tool\_c89cc\_val "$\_dot\_field"; local \_fn60=$REPLY |
|  | local \_foff=0 |
|  | \_tool\_c89cc\_field\_off "$\_fn60"; \_foff=$REPLY |
|  | # Add field offset if nonzero |
|  | case "$\_foff" in 0) ;; \*) |
|  | \_tool\_c89cc\_emit "48 05" # add rax, imm32 |
|  | \_tool\_c89cc\_emit\_le32 $\_foff;; esac |
|  | \_tool\_c89cc\_emit "48 8B 00";; # mov rax, [rax] |
|  |  |
|  | C61) # Arrow access: p->field → deref pointer + field offset |
|  | \_tool\_c89cc\_children "$\_n" |
|  | local \_arr\_base="${REPLY%% \*}" \_arr\_field="${REPLY#\* }" |
|  | \_tool\_c89cc\_expr "$\_arr\_base" # rax = pointer value (address) |
|  | \_tool\_c89cc\_val "$\_arr\_field"; local \_fn61=$REPLY |
|  | local \_foff=0 |
|  | \_tool\_c89cc\_field\_off "$\_fn61"; \_foff=$REPLY |
|  | # Add field offset if nonzero |
|  | case "$\_foff" in 0) ;; \*) |
|  | \_tool\_c89cc\_emit "48 05" # add rax, imm32 |
|  | \_tool\_c89cc\_emit\_le32 $\_foff;; esac |
|  | \_tool\_c89cc\_emit "48 8B 00";; # mov rax, [rax] |
|  |  |
|  | C45) # String literal |
|  | \_tool\_c89cc\_add\_string "$\_v" |
|  | local \_str\_id=$REPLY |
|  | # Load address of string: will be patched during ELF generation |
|  | # For now: emit mov rax, imm64 with placeholder |
|  | \_tool\_c89cc\_emit "48 B8" # movabs rax, imm64 |
|  | eval "local \_soff=\$\_STR\_OFF\_$\_str\_id" |
|  | # Record string relocation (patched after code+data layout is known) |
|  | \_RELOCS="$\_RELOCS S${\_IP}=STR${\_str\_id}" |
|  | \_tool\_c89cc\_emit "00 00 00 00 00 00 00 00";; # placeholder |
|  |  |
|  | C46) # Character literal: 'x' → ASCII value |
|  | local \_charval |
|  | case "$\_v" in |
|  | '\\n') \_charval=10;; |
|  | '\\t') \_charval=9;; |
|  | '\\0') \_charval=0;; |
|  | '\\\\') \_charval=92;; |
|  | "\\'") \_charval=39;; |
|  | '\\r') \_charval=13;; |
|  | \*) \_tool\_c89cc\_c2d "$\_v"; \_charval=$REPLY;; |
|  | esac |
|  | \_tool\_c89cc\_emit "48 C7 C0" |
|  | \_tool\_c89cc\_emit\_le32 $\_charval;; |
|  |  |
|  | C43) # Parenthesized expression: ( expr ) |
|  | \_tool\_c89cc\_children "$\_n" |
|  | \_tool\_c89cc\_expr "$REPLY";; |
|  |  |
|  | C41) # sizeof\_expr → compile-time constant |
|  | \_tool\_c89cc\_children "$\_n" |
|  | # sizeof\_body children are type names; default to 8 (pointer size) |
|  | \_tool\_c89cc\_emit "48 C7 C0" |
|  | \_tool\_c89cc\_emit\_le32 8;; |
|  |  |
|  | \*) ;; # Unknown — emit 0 |
|  | esac |
|  | } |
|  |  |
|  | # ============================================================ |
|  | # ELF64 Header Generation |
|  | # ============================================================ |
|  | \_BASE\_ADDR=4194304 # 0x400000 |
|  | \_HDR\_SIZE=120 # 64 (ELF) + 56 (1 program header) |
|  |  |
|  | \_tool\_c89cc\_write\_elf () { |
|  | local \_code\_size=$\_IP |
|  | local \_str\_size=$(( ${#\_STR\_DATA} / 2 )) |
|  | local \_glob\_size=$(( ${#\_GLOB\_DATA} / 2 )) |
|  | local \_data\_size=$(( \_str\_size + \_glob\_size )) |
|  | local \_total\_size=$(( \_HDR\_SIZE + \_code\_size + \_data\_size )) |
|  | local \_entry=$(( \_BASE\_ADDR + \_HDR\_SIZE )) |
|  | # Data starts right after code |
|  | local \_str\_base=$(( \_BASE\_ADDR + \_HDR\_SIZE + \_code\_size )) |
|  | local \_glob\_base=$(( \_str\_base + \_str\_size )) |
|  |  |
|  | # ELF64 Header (64 bytes) |
|  | # e\_ident: magic + class + data + version + OS/ABI + padding |
|  | \_out\_byte 127; \_out\_byte 69; \_out\_byte 76; \_out\_byte 70 # \x7fELF |
|  | \_out\_byte 2; \_out\_byte 1; \_out\_byte 1; \_out\_byte 0 # 64-bit, LE, v1, SysV |
|  | \_out\_byte 0; \_out\_byte 0; \_out\_byte 0; \_out\_byte 0 # padding |
|  | \_out\_byte 0; \_out\_byte 0; \_out\_byte 0; \_out\_byte 0 |
|  |  |
|  | # e\_type (2) + e\_machine (2) + e\_version (4) |
|  | \_out\_byte 2; \_out\_byte 0 # ET\_EXEC |
|  | \_out\_byte 62; \_out\_byte 0 # EM\_X86\_64 |
|  | \_out\_byte 1; \_out\_byte 0; \_out\_byte 0; \_out\_byte 0 # EV\_CURRENT |
|  |  |
|  | # e\_entry (8 bytes, little-endian) |
|  | \_tool\_c89cc\_le64 $\_entry |
|  |  |
|  | # e\_phoff (8) = 64 (right after ELF header) |
|  | \_tool\_c89cc\_le64 64 |
|  |  |
|  | # e\_shoff (8) = 0 (no section headers) |
|  | \_tool\_c89cc\_le64 0 |
|  |  |
|  | # e\_flags (4) + e\_ehsize (2) + e\_phentsize (2) |
|  | \_out\_byte 0; \_out\_byte 0; \_out\_byte 0; \_out\_byte 0 # flags |
|  | \_out\_byte 64; \_out\_byte 0 # ehsize = 64 |
|  | \_out\_byte 56; \_out\_byte 0 # phentsize = 56 |
|  |  |
|  | # e\_phnum (2) + e\_shentsize (2) + e\_shnum (2) + e\_shstrndx (2) |
|  | \_out\_byte 1; \_out\_byte 0 # 1 program header |
|  | \_out\_byte 0; \_out\_byte 0 # shentsize = 0 |
|  | \_out\_byte 0; \_out\_byte 0 # shnum = 0 |
|  | \_out\_byte 0; \_out\_byte 0 # shstrndx = 0 |
|  |  |
|  | # Program Header (56 bytes) |
|  | # p\_type (4) = PT\_LOAD |
|  | \_out\_byte 1; \_out\_byte 0; \_out\_byte 0; \_out\_byte 0 |
|  |  |
|  | # p\_flags (4) = PF\_R | PF\_W | PF\_X = 7 |
|  | \_out\_byte 7; \_out\_byte 0; \_out\_byte 0; \_out\_byte 0 |
|  |  |
|  | # p\_offset (8) = 0 (load from start of file) |
|  | \_tool\_c89cc\_le64 0 |
|  |  |
|  | # p\_vaddr (8) = base address |
|  | \_tool\_c89cc\_le64 $\_BASE\_ADDR |
|  |  |
|  | # p\_paddr (8) = same |
|  | \_tool\_c89cc\_le64 $\_BASE\_ADDR |
|  |  |
|  | # p\_filesz (8) = total file size |
|  | \_tool\_c89cc\_le64 $\_total\_size |
|  |  |
|  | # p\_memsz (8) = same (no BSS yet) |
|  | \_tool\_c89cc\_le64 $\_total\_size |
|  |  |
|  | # p\_align (8) = 0x1000 |
|  | \_tool\_c89cc\_le64 4096 |
|  |  |
|  | # Code section |
|  | \_tool\_c89cc\_write\_code |
|  |  |
|  | # String data section |
|  | case "$\_STR\_DATA" in ?\*) \_tool\_c89cc\_write\_hex\_str "$\_STR\_DATA";; esac |
|  |  |
|  | # Global data section |
|  | case "$\_GLOB\_DATA" in ?\*) \_tool\_c89cc\_write\_hex\_str "$\_GLOB\_DATA";; esac |
|  | } |
|  |  |
|  | # Write a 64-bit little-endian value as raw bytes |
|  | \_tool\_c89cc\_le64 () { |
|  | local \_v=$1 \_i=0 |
|  | while test $\_i -lt 8; do |
|  | \_out\_byte $(( \_v % 256 )) |
|  | \_v=$(( \_v / 256 )) |
|  | \_i=$((\_i + 1)) |
|  | done |
|  | } |
|  |  |
|  | # Convert 2-char hex to decimal. Result in REPLY. |
|  | \_tool\_c89cc\_hex2dec () { |
|  | local \_h1="${1%?}" \_h2="${1#?}" \_d1 \_d2 |
|  | case "$\_h1" in |
|  | 0) \_d1=0;; 1) \_d1=1;; 2) \_d1=2;; 3) \_d1=3;; 4) \_d1=4;; |
|  | 5) \_d1=5;; 6) \_d1=6;; 7) \_d1=7;; 8) \_d1=8;; 9) \_d1=9;; |
|  | [Aa]) \_d1=10;; [Bb]) \_d1=11;; [Cc]) \_d1=12;; |
|  | [Dd]) \_d1=13;; [Ee]) \_d1=14;; [Ff]) \_d1=15;; esac |
|  | case "$\_h2" in |
|  | 0) \_d2=0;; 1) \_d2=1;; 2) \_d2=2;; 3) \_d2=3;; 4) \_d2=4;; |
|  | 5) \_d2=5;; 6) \_d2=6;; 7) \_d2=7;; 8) \_d2=8;; 9) \_d2=9;; |
|  | [Aa]) \_d2=10;; [Bb]) \_d2=11;; [Cc]) \_d2=12;; |
|  | [Dd]) \_d2=13;; [Ee]) \_d2=14;; [Ff]) \_d2=15;; esac |
|  | REPLY=$(( \_d1 \* 16 + \_d2 )) |
|  | } |
|  |  |
|  |  |
|  | # Write the code buffer as raw bytes |
|  | \_tool\_c89cc\_write\_code () { |
|  | local \_i=0 |
|  | while test $\_i -lt $\_IP; do |
|  | eval "\_tool\_c89cc\_hex2dec \"\$\_CB\_$\_i\"" |
|  | \_out\_byte "$REPLY" |
|  | \_i=$((\_i + 1)) |
|  | done |
|  | } |
|  |  |
|  | # Write a hex-pair string as raw bytes (for string/global data sections) |
|  | \_tool\_c89cc\_write\_hex\_str () { |
|  | local \_s="${1:-}" \_c1 \_c2 |
|  | while test ${#\_s} -gt 0; do |
|  | \_c1="${\_s%"${\_s#?}"}"; \_s="${\_s#?}" |
|  | \_c2="${\_s%"${\_s#?}"}"; \_s="${\_s#?}" |
|  | \_tool\_c89cc\_hex2dec "$\_c1$\_c2" |
|  | \_out\_byte "$REPLY" |
|  | done |
|  | } |
|  |  |
|  | # ============================================================ |
|  | # Entry Point |
|  | # ============================================================ |
|  | \_tool\_c89cc\_init () { |
|  | # Ensure word splitting works for for-loops |
|  | IFS=' ' |
|  |  |
|  | # Register common struct layouts (for hex2 compatibility) |
|  | \_tool\_c89cc\_struct\_def "input\_files" |
|  | \_tool\_c89cc\_struct\_field "next" 8 |
|  | \_tool\_c89cc\_struct\_field "filename" 8 |
|  | \_tool\_c89cc\_struct\_def "entry" |
|  | \_tool\_c89cc\_struct\_field "next" 8 |
|  | \_tool\_c89cc\_struct\_field "target" 8 |
|  | \_tool\_c89cc\_struct\_field "name" 8 |
|  | } |
|  |  |
|  | # ============================================================ |
|  | # Entry Point |
|  | # ============================================================ |
|  | cc\_c89 () { |
|  | # Read AST from stdin (line-by-line to avoid eval size limits) |
|  | while IFS='' read -r \_ast\_line; do eval "$\_ast\_line"; done |
|  | case "${\_ast\_line:-}" in ?\*) eval "$\_ast\_line";; esac |
|  |  |
|  | \_tool\_c89cc\_init |
|  |  |
|  | # ELF mode: emit \_start entry point |
|  | \_tool\_c89cc\_label "\_start" |
|  | \_tool\_c89cc\_emit "E8"; \_tool\_c89cc\_reloc\_rel32 "main" |
|  | \_tool\_c89cc\_emit "48 89 C7" |
|  | \_tool\_c89cc\_emit "48 C7 C0"; \_tool\_c89cc\_emit\_le32 60 |
|  | \_tool\_c89cc\_emit "0F 05" |
|  | \_tool\_c89cc\_node 0 |
|  | \_tool\_c89cc\_fixup |
|  | \_tool\_c89cc\_write\_elf |
|  | } |
|  |  |
|  | tool\_c89cc () { cc\_c89; } |
|  |  |
|  | # --- core/footer.sh --- |
|  | # ksh93 fix: re-declare functions via eval. |
|  | # In ksh93, functions defined via `. file` don't get alias expansion. |
|  | # Re-declaring via eval fixes this. Two modes: |
|  | # - Dynamic-scoped (POSIX name(){}): functions that read/write caller-scope |
|  | # variables (\_LN, \_COL, \_SRC\*, CONSUMED, V\*, X\*, etc.) or entry points |
|  | # whose locals must be visible to callees (parsers, generators, tests). |
|  | # - Static-scoped (AT&T function name {}): everything else, especially |
|  | # recursive emitters (\_\*\_emit) that need isolated locals per call frame. |
|  | # Convention: new utility functions (str\_\*, io\_\*, ds\_\*, codegen\_\*, opt\_\*) |
|  | # use only their own locals + REPLY, so static scoping (the default) is correct. |
|  | \_Ldefn\_fix= |
|  | eval "\_Ldefn\_fix(){ typeset \_Ldefn\_fix=local;} 2>/dev/null" |
|  | \_Ldefn\_fix 2>/dev/null || : |
|  | case $\_Ldefn\_fix in "local") |
|  | \_Ldefn\_fix () { |
|  | case "$1" in \_Ldefn\_fix) return;; esac |
|  | \_Ldefn\_fix="$(typeset -f "$1" 2>/dev/null)" || return 0 |
|  | \_Ldefn\_fix="${\_Ldefn\_fix#\*\{}" |
|  | case "$1" in |
|  | \*\_parser|ast\_out|\_error|\_nlcount|\_numck|\_ast\_core\_pars\_epilogue) |
|  | eval "$1 () {${\_Ldefn\_fix}" 2>/dev/null || :;; |
|  | gen\_\*|test\_\*|unit\_\*|integration\_\*|full\_\*) |
|  | eval "$1 () {${\_Ldefn\_fix}" 2>/dev/null || :;; |
|  | \_bnf\_gen\_\*|\_shell\_common\_stripq|\_shell\_common\_shdelim) |
|  | eval "$1 () {${\_Ldefn\_fix}" 2>/dev/null || :;; |
|  | \*) |
|  | eval "function $1 {${\_Ldefn\_fix}" 2>/dev/null || :;; |
|  | esac |
|  | } |
|  | IFS=' |
|  | ' |
|  | for \_Ldefn\_fix in $(typeset +f); do |
|  | \_Ldefn\_fix "${\_Ldefn\_fix%%"()"\*}" |
|  | done |
|  | IFS='' |
|  | ;; |
|  | esac |
|  | unset \_Ldefn\_fix |
|  | unset -f \_Ldefn\_fix 2>/dev/null || : |
|  |  |
|  | # --- built-in libc.c --- |
|  | \_BUILTIN\_LIBC=' |
|  | /\* ============================================================ |
|  | \* Mini-libc: syscall-only C library for x86-64 Linux |
|  | \* ============================================================ |
|  | \* No external dependencies. Compiled by gen/c89cc.sh. |
|  | \* |
|  | \* Build: printf '\'''\'' | cat lib/libc.c YOURPROG.c | sh gen/c89.sh | sh gen/c89cc.sh > a.out |
|  | \*/ |
|  |  |
|  | /\* ============================================================ |
|  | \* Syscall wrappers |
|  | \* ============================================================ |
|  | \* Linux x86-64 syscall numbers from <asm/unistd\_64.h> |
|  | \*/ |
|  |  |
|  | int sys\_read(int fd, char \*buf, int count) { |
|  | return \_\_syscall(0, fd, buf, count); |
|  | } |
|  |  |
|  | int sys\_write(int fd, char \*buf, int count) { |
|  | return \_\_syscall(1, fd, buf, count); |
|  | } |
|  |  |
|  | int sys\_open(char \*path, int flags, int mode) { |
|  | return \_\_syscall(2, path, flags, mode); |
|  | } |
|  |  |
|  | int sys\_close(int fd) { |
|  | return \_\_syscall(3, fd); |
|  | } |
|  |  |
|  | int sys\_brk(int addr) { |
|  | return \_\_syscall(12, addr); |
|  | } |
|  |  |
|  | int sys\_pipe(int \*fds) { |
|  | return \_\_syscall(22, fds); |
|  | } |
|  |  |
|  | int sys\_dup2(int oldfd, int newfd) { |
|  | return \_\_syscall(33, oldfd, newfd); |
|  | } |
|  |  |
|  | int sys\_fork() { |
|  | return \_\_syscall(57); |
|  | } |
|  |  |
|  | int sys\_execve(char \*path, char \*\*argv, char \*\*envp) { |
|  | return \_\_syscall(59, path, argv, envp); |
|  | } |
|  |  |
|  | int sys\_exit(int code) { |
|  | return \_\_syscall(60, code); |
|  | } |
|  |  |
|  | int sys\_wait4(int pid, int \*status, int options, int rusage) { |
|  | return \_\_syscall(61, pid, status, options, rusage); |
|  | } |
|  |  |
|  | int sys\_getcwd(char \*buf, int size) { |
|  | return \_\_syscall(79, buf, size); |
|  | } |
|  |  |
|  | int sys\_chdir(char \*path) { |
|  | return \_\_syscall(80, path); |
|  | } |
|  |  |
|  | /\* ============================================================ |
|  | \* String operations |
|  | \* ============================================================ \*/ |
|  |  |
|  | int strlen(char \*s) { |
|  | int n = 0; |
|  | while (\*s) { n += 1; s = s + 1; } |
|  | return n; |
|  | } |
|  |  |
|  | int strcmp(char \*a, char \*b) { |
|  | while (\*a && \*a == \*b) { a = a + 1; b = b + 1; } |
|  | return \*a - \*b; |
|  | } |
|  |  |
|  | int strncmp(char \*a, char \*b, int n) { |
|  | while (n > 0 && \*a && \*a == \*b) { a = a + 1; b = b + 1; n -= 1; } |
|  | if (n == 0) return 0; |
|  | return \*a - \*b; |
|  | } |
|  |  |
|  | char \*strcpy(char \*dst, char \*src) { |
|  | char \*d = dst; |
|  | while (\*src) { \*d = \*src; d = d + 1; src = src + 1; } |
|  | \*d = 0; |
|  | return dst; |
|  | } |
|  |  |
|  | char \*strcat(char \*dst, char \*src) { |
|  | char \*d = dst; |
|  | while (\*d) d = d + 1; |
|  | while (\*src) { \*d = \*src; d = d + 1; src = src + 1; } |
|  | \*d = 0; |
|  | return dst; |
|  | } |
|  |  |
|  | char \*strchr(char \*s, int c) { |
|  | while (\*s) { |
|  | if (\*s == c) return s; |
|  | s = s + 1; |
|  | } |
|  | if (c == 0) return s; |
|  | return 0; |
|  | } |
|  |  |
|  | char \*memcpy(char \*dst, char \*src, int n) { |
|  | char \*d = dst; |
|  | while (n > 0) { \*d = \*src; d = d + 1; src = src + 1; n -= 1; } |
|  | return dst; |
|  | } |
|  |  |
|  | char \*memset(char \*dst, int c, int n) { |
|  | char \*d = dst; |
|  | while (n > 0) { \*d = c; d = d + 1; n -= 1; } |
|  | return dst; |
|  | } |
|  |  |
|  | /\* ============================================================ |
|  | \* Memory allocator (bump + free-list via brk) |
|  | \* ============================================================ |
|  | \* Each allocation has an 8-byte header storing the usable size. |
|  | \* free() returns blocks to a binned free-list (10 size classes: |
|  | \* 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096). |
|  | \* malloc() checks the free-list before bumping the heap. |
|  | \*/ |
|  |  |
|  | int \_heap\_start; |
|  | int \_heap\_cur; |
|  | int \_heap\_end; |
|  |  |
|  | /\* Free-list bins: 10 classes (8..4096), each a singly-linked list. |
|  | \* Freed blocks store the "next" pointer in their first 8 bytes. |
|  | \* Allocated at first malloc call (can'\''t use global array, compiler |
|  | \* allocates only 8 bytes per global regardless of array size). \*/ |
|  | int \*\_free\_bins; |
|  |  |
|  | int \_size\_class(int size) { |
|  | /\* Return bin index for 8-aligned size, or -1 if too large \*/ |
|  | int bin; int s; |
|  | bin = 0; s = 8; |
|  | while (s < size) { s = s \* 2; bin = bin + 1; if (bin >= 10) return -1; } |
|  | return bin; |
|  | } |
|  |  |
|  | int malloc(int size) { |
|  | int cur; |
|  | int new\_end; |
|  | int \*hp; |
|  | int bin; |
|  | if (\_heap\_start == 0) { |
|  | \_heap\_start = sys\_brk(0); |
|  | \_heap\_cur = \_heap\_start; |
|  | \_heap\_end = sys\_brk(\_heap\_start + 8388608); |
|  | /\* Allocate free-list bins (10 entries, zeroed) \*/ |
|  | \_free\_bins = \_heap\_cur; |
|  | \_heap\_cur = \_heap\_cur + 80; |
|  | bin = 0; while (bin < 10) { \_free\_bins[bin] = 0; bin = bin + 1; } |
|  | } |
|  | size = (size + 7) & -8; |
|  | bin = \_size\_class(size); |
|  | if (bin >= 0) { |
|  | cur = \_free\_bins[bin]; |
|  | if (cur != 0) { |
|  | hp = cur; |
|  | \_free\_bins[bin] = hp[0]; |
|  | hp = cur - 8; |
|  | hp[0] = size; |
|  | return cur; |
|  | } |
|  | } |
|  | /\* Bump allocate with 8-byte size header \*/ |
|  | cur = \_heap\_cur; |
|  | \_heap\_cur = cur + size + 8; |
|  | if (\_heap\_cur > \_heap\_end) { |
|  | new\_end = \_heap\_cur + 16777216; |
|  | \_heap\_end = sys\_brk(new\_end); |
|  | } |
|  | hp = cur; |
|  | hp[0] = size; |
|  | return cur + 8; |
|  | } |
|  |  |
|  | void free(char \*ptr) { |
|  | int size; |
|  | int bin; |
|  | int \*hp; |
|  | if (ptr == 0) return; |
|  | /\* Only free heap-allocated pointers (skip string literals, etc.) \*/ |
|  | if (ptr <= \_heap\_start || ptr >= \_heap\_cur) return; |
|  | hp = ptr - 8; |
|  | size = hp[0]; /\* read header \*/ |
|  | bin = \_size\_class(size); |
|  | if (bin < 0) return; /\* oversized: leak \*/ |
|  | hp = ptr; |
|  | hp[0] = \_free\_bins[bin]; /\* store next ptr in block \*/ |
|  | \_free\_bins[bin] = ptr; |
|  | } |
|  |  |
|  | /\* ============================================================ |
|  | \* Temporary arena (bulk-reset between commands) |
|  | \* ============================================================ \*/ |
|  |  |
|  | int \_tmp\_base; |
|  | int \_tmp\_cur; |
|  | int \_tmp\_size; |
|  |  |
|  | void tmp\_init(int size) { |
|  | \_tmp\_base = malloc(size); |
|  | \_tmp\_cur = \_tmp\_base; |
|  | \_tmp\_size = size; |
|  | } |
|  |  |
|  | int tmp\_alloc(int size) { |
|  | int cur; |
|  | size = (size + 7) & -8; |
|  | cur = \_tmp\_cur; |
|  | \_tmp\_cur = cur + size; |
|  | if (\_tmp\_cur > \_tmp\_base + \_tmp\_size) { |
|  | \_tmp\_cur = cur; |
|  | return malloc(size); |
|  | } |
|  | return cur; |
|  | } |
|  |  |
|  | void tmp\_reset() { |
|  | \_tmp\_cur = \_tmp\_base; |
|  | } |
|  |  |
|  | /\* ============================================================ |
|  | \* I/O helpers |
|  | \* ============================================================ \*/ |
|  |  |
|  | /\* Report stack + heap usage to stderr \*/ |
|  | void mem\_report() { |
|  | int stack\_var; |
|  | fputs("MEM: heap=", 2); |
|  | print\_int((\_heap\_cur - \_heap\_start) / 1024); |
|  | fputs("K stack\_approx=", 2); |
|  | /\* &stack\_var gives approximate stack pointer \*/ |
|  | print\_int(&stack\_var); |
|  | fputs("\n", 2); |
|  | } |
|  |  |
|  | int putchar(int c) { |
|  | char buf; |
|  | \*(&buf) = c; |
|  | sys\_write(1, &buf, 1); |
|  | return c; |
|  | } |
|  |  |
|  | int puts(char \*s) { |
|  | sys\_write(1, s, strlen(s)); |
|  | putchar(10); |
|  | return 0; |
|  | } |
|  |  |
|  | int fputs(char \*s, int fd) { |
|  | sys\_write(fd, s, strlen(s)); |
|  | return 0; |
|  | } |
|  |  |
|  | int getchar() { |
|  | char buf; |
|  | int n; |
|  | n = sys\_read(0, &buf, 1); |
|  | if (n <= 0) return -1; |
|  | return \*(&buf); |
|  | } |
|  |  |
|  | /\* Print unsigned decimal integer (recursive to avoid local arrays) \*/ |
|  | void print\_uint(int n) { |
|  | if (n >= 10) print\_uint(n / 10); |
|  | putchar(48 + n % 10); |
|  | } |
|  |  |
|  | /\* Print signed decimal integer \*/ |
|  | void print\_int(int n) { |
|  | if (n < 0) { |
|  | putchar(45); |
|  | print\_uint(0 - n); |
|  | } else { |
|  | print\_uint(n); |
|  | } |
|  | } |
|  | ' |
|  |  |
|  | # --- main --- |
|  | \_no\_libc=0 |
|  | case "${1:-}" in --no-libc) \_no\_libc=1; shift;; esac |
|  |  |
|  | if test $\_no\_libc -eq 1; then |
|  | c89\_parser | cc\_c89 |
|  | else |
|  | { \_printr1 "$\_BUILTIN\_LIBC"; /bin/cat; } | c89\_parser | cc\_c89 |
|  | fi |