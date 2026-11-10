---
title: "FreeOberon – Open-Source, Cross-Platform, Free Pascal/Turbo Pascal-Like Language"
url: https://github.com/kekcleader/FreeOberon
clipped: 2026-06-17 00:48:10
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [FreeOberon – Open-Source, Cross-Platform, Free Pascal/Turbo Pascal-Like Language](https://github.com/kekcleader/FreeOberon)

## Digest Summary
Free Oberon is a cross‑platform integrated development environment (IDE) for the Oberon programming language, styled after classic Pascal pseudo‑graphic screens. It runs on Windows, macOS, and Linux and includes the console‑based compiler fob.  

**Key dependencies** (Linux): Allegro 5 development packages, Git, GCC. Installation commands are provided for Debian/Ubuntu/Mint (apt), Fedora (dnf), Arch (pacman), and openSUSE (zypper).  

**Installation steps**: download the tar.gz archive from free.oberon.org or the latest ZIP from the GitHub repo (https://github.com/kekcleader/FreeOberon), unpack to a directory without non‑Latin characters, rename to FreeOberon, and run install.sh. An optional Bash alias (`fo`) can launch the IDE.  

**Usage**: source files are stored in a `Programs` subdirectory; compiled binaries go to `bin` (or alongside the main module if outside `Programs`). Press F9 to compile/run; the IDE auto‑links multi‑module projects and opens files with compilation errors, indicating line and message. Scripts `Data/bin/compile.sh` (Linux) and `Data\bin\compile.bat` (Windows) handle the build process.

## Discussion Summary
The comment reflects nostalgic affection for early Pascal environments, describing a sense of empowerment while acknowledging that newer languages like C and Perl ultimately surpass Turbo Pascal in capability. It expresses enthusiasm for exploring Oberon as a compact, powerful language and anticipates testing it on a Mac. At the same time, the author criticizes the project’s website for featuring a Soviet‑parliament image, labeling the choice as in poor taste. Overall, the tone blends fond recollection, pragmatic assessment, eager interest in Oberon, and disapproval of controversial visual branding.

---

## Full Article

Free Oberon programming environment
===================================

» [free.oberon.org](https://free.oberon.org/en)

Oberon is a general-purpose programming language–the direct descendant of Pascal and Modula-2. It is both simpler and much more powerful than Pascal and Modula.

Free Oberon is a cross-platform integrated development environment for the Oberon programming language, designed in the classic pseudo-graphic style–the famous blue screen of Pascal. Available for Windows, macOS and Linux.

Fob is a convenient console-based Oberon compiler.

[![Free Oberon screenshot](https://camo.githubusercontent.com/51174850e04a81eb65a9e0624ddf3facf245092676b4cf9b0442ce59cff1f2cb/687474703a2f2f667265652e6f6265726f6e2e6f72672f696d616765732f73637265656e73686f742e706e67)](https://camo.githubusercontent.com/51174850e04a81eb65a9e0624ddf3facf245092676b4cf9b0442ce59cff1f2cb/687474703a2f2f667265652e6f6265726f6e2e6f72672f696d616765732f73637265656e73686f742e706e67)

[![Game of Life animation in Oberon](https://camo.githubusercontent.com/6272ab467b820df6ae1470b1a6e4e15c9ade0011efd43cacee92c02897421cd9/687474703a2f2f667265652e6f6265726f6e2e6f72672f696d616765732f6c6966652e676966)](https://camo.githubusercontent.com/6272ab467b820df6ae1470b1a6e4e15c9ade0011efd43cacee92c02897421cd9/687474703a2f2f667265652e6f6265726f6e2e6f72672f696d616765732f6c6966652e676966)

*See English text below.*

Среда программирования Free Oberon
==================================

Оберон — язык программирования общего назначения, прямой наследник Паскаля и Модулы-2. Он одновременно и проще, и намного мощнее, чем Паскаль и Модула.

Free Oberon представляет собой кроссплатформенную интегрированную среду разработки на языке программирования Оберон, выполненную в классическом псевдографическом стиле — знаменитого синего экрана Паскаля. Поставляется для Виндоуса, Мак-ОС и Линукса.

Fob — это консольный компилятор языка Оберон.

1. Зависимости:

   Allegro (пакеты разработки), Git, GCC

   На ОС Дебиан / Убунту / Линукс Минт и т. п.:

   ```
   sudo apt-get update
   sudo apt-get install -y git gcc libc-dev liballegro5-dev
   ```

   или:

   ```
   su
   apt-get update
   apt-get install -y git gcc libc-dev liballegro5-dev
   ```

   На ОС Федора:

   ```
   sudo dnf install -y git gcc glibc-devel allegro5-devel allegro5-addon-image allegro5-addon-audio allegro5-addon-acodec allegro5-addon-dialog allegro5-devel allegro5-addon-image-devel allegro5-addon-audio-devel allegro5-addon-acodec-devel allegro5-addon-dialog-devel
   ```

   На Арч Линукс:

   ```
   sudo pacman -Sy git gcc pkgconf glibc allegro
   ```

   На Опен Сюзе:

   ```
   sudo zypper install -y git gcc glibc-devel liballegro5_2-devel liballegro_audio5_2-devel liballegro_image5_2-devel liballegro_primitives5_2-devel liballegro_dialog5_2-devel liballegro_acodec5_2-devel liballegro_acodec5_2-devel liballegro_font5_2-devel
   ```
2. Скачайте Free Oberon в виде архива tar.gz с сайта
   [free.oberon.org](https://free.oberon.org/download)
   и распакуйте его в домашнем каталоге (или в любом другом месте).

   Вариант (новейшая сборка):

   На сайте <https://github.com/kekcleader/FreeOberon.git>
   нажмите зелёную кнопку «Code» и «Download ZIP»,
   распакуйте архив в домашнем каталоге.
   Переименуйте каталог `FreeOberon-main` в `FreeOberon`.
3. Находясь в распакованном каталоге, запустите `install.sh`.

4. (по желанию) Допишите в конец файла `~/.bashrc` строчку:

```
alias fo='cd ~/FreeOberon;./FreeOberon'
```

Это позволит запускать Free Oberon командой `fo`.

Для запуска Free Oberon на конкретном языке, укажите язык (en или ru):

или

Скачайте архив с сайта [free.oberon.org](https://free.oberon.org), распакуйте его в по такому пути, в котором нет не-латинских букв, и запустите `FreeOberon.exe`.

Примечание. Если вы хотите самостоятельно собрать версию Free Oberon под ОС Windows из исходных кодов, обратитесь к приложению A [документации Free Oberon на free.oberon.org](http://free.oberon.org/files/FreeOberon_v1.1.0.pdf).

Запустите Free Oberon и наберите текст программного модуля на языке Оберон (или откройте файл с примером программы, например `Life.Mod`). Нажмите `F9`, чтобы скомпилировать и запустить программу.
Файлы с исходным кодом ваших программ сохраняются в подкаталоге `Programs`, а скомпилированные исполняемые файлы сохраняются в подкаталоге `bin`. Сценарий `Data/bin/compile.sh` (`Data\bin\compile.bat`) используется на Линуксе (Виндоусе) в ходе компиляции. Вы можете править эти сценарии.

Можно писать программы, состоящие из нескольких модулей. Откройте главный модуль и нажмите `F9`. Free Oberon автоматически скомпилирует и скомпонует их в правильном порядке.

Если вы компилируете программу, файл главного модуля которой не находится непосредственно в подкаталоге `Programs`, то скомпилированный исполнимый файл будет находится рядом с ним, а не в подкаталоге `_Build`.

Если в одном из модулей программы будет найдена ошибка, соответствующий файл откроется, место и характер ошибки будут указаны. Чтобы перекомпилировать, снова перейдите к окну главного модуля и нажмите `F9`.

[История версий](https://github.com/kekcleader/FreeOberon/blob/main/HISTORY.md)

---

*ENGLISH*

1. Dependencies:

   Allegro (development packages), Git, GCC

   On OS Debian / Ubuntu / Linux Mint and so on:

   ```
   sudo apt-get update
   sudo apt-get install -y git gcc libc-dev liballegro5-dev
   ```

   or:

   ```
   su
   apt-get update
   apt-get install -y git gcc libc-dev liballegro5-dev
   ```

   On OS Fedora:

   ```
   sudo dnf install -y git gcc glibc-devel allegro5-devel allegro5-addon-image allegro5-addon-audio allegro5-addon-acodec allegro5-addon-dialog allegro5-devel allegro5-addon-image-devel allegro5-addon-audio-devel allegro5-addon-acodec-devel allegro5-addon-dialog-devel argro5-addon-dialog-devel
   ```

   On Arch Linux:

   ```
   sudo pacman -Sy git gcc pkgconf glibc allegro
   ```

   On openSUSE:

   ```
   sudo zypper install -y git gcc glibc-devel liballegro5_2-devel liballegro_audio5_2-devel liballegro_image5_2-devel liballegro_primitives5_2-devel liballegro_dialog5_2-devel liballegro_acodec5_2-devel liballegro_acodec5_2-devel liballegro_font5_2-devel
   ```
2. Download Free Oberon in tar.gz format from
   [free.oberon.org](https://free.oberon.org/en/download)
   and unpack it inside home directory (or in any other place).

   Option (edge build):

   Go to <https://github.com/kekcleader/FreeOberon.git> and
   click the green button labeled "Code" and then click "Download ZIP",
   unpack the archive inside your home directory.
   Rename directory `FreeOberon-main` to `FreeOberon`.
3. Inside the unpacked directory, run `install.sh`.

4. (optional) Append the following line to the end of file `~/.bashrc`:

```
alias fo='cd ~/FreeOberon;./FreeOberon'
```

This will allow you to launch Free Oberon using the `fo` command.

To run Free Oberon in a specific language, specify it (en or ru):

or

Download Free Oberon in a ZIP archive (from [free.oberon.org](https://free.oberon.org/en)), extract it to a path on the disk that does not have any non-latin characters in it, and lauch `FreeOberon.exe`.

Note. If you want to recompile Free Oberon under Windows from the source code, refer to Appendix A of the [Free Oberon documentation on free.oberon.org](https://free.oberon.org/files/FreeOberon_v1.1.0_en.pdf).

Run Free Oberon and type the text of an Oberon module (or open a sample program such as `Life.Mod`) and press `F9` to compile and run the program.
The source code files of your programs are saved in the `Programs` subdirectory, and the compiled executables are saved in the `bin` subdirectory. The script `Data/bin/compile.sh` (`Data\bin\compile.bat`) is used on Linux (Windows) for compilation. You can edit these scripts.

You can write programs consisting of several modules. Open the main module and press `F9`. Free Oberon automatically compiles and links them in the correct order.

If you compile a program whose main module file is not directly in the `Programs` subdirectory, the compiled executable will be located next to it and not in the `_Build` subdirectory.

If an error occurres during the compilation of one of the modules, the corresponding file will be open and error position and message will be indicated. To recompile, go to the main module window again and press `F9`.

[Version history](https://github.com/kekcleader/FreeOberon/blob/main/HISTORY.md)