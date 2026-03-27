# 02. Cursor IDE Keyboard Shortcuts Reference

_A comprehensive guide to Cursor IDE shortcuts for Mac and Windows_

Based on research from [Cursor101](https://cursor101.com/cursor/cheat-sheet), [Starmorph Blog](https://blog.starmorph.com/blog/vs-code-mac-keyboard-shortcuts-guide-for-developers), and [Mehmet Baykar](https://www.mehmetbaykar.com/posts/top-15-cursor-shortcuts-to-speed-up-development/).

- --

## 📑 Table of Contents

1. [🤖 Cursor AI-Specific Features](#-cursor-ai-specific-features)
   - [Essential AI Shortcuts](#essential-ai-shortcuts)
   - [AI Code Completion (Cursor Tab)](#ai-code-completion-cursor-tab)
   - [AI Context & References](#ai-context--references)
   - [AI Inline Editing](#ai-inline-editing)
   - [AI @ Symbols (Context References)](#ai--symbols-context-references)
2. [📂 General IDE Operations](#-general-ide-operations)
   - [Command Palette & Settings](#command-palette--settings)
   - [Window Management](#window-management)
3. [✏️ Basic Editing](#️-basic-editing)
   - [Line Operations](#line-operations)
   - [Text Navigation](#text-navigation)
   - [Indentation & Formatting](#indentation--formatting)
   - [Comments](#comments)
4. [🎯 Multi-Cursor & Selection](#-multi-cursor--selection)
   - [Multi-Cursor Operations](#multi-cursor-operations)
   - [Text Selection](#text-selection)
   - [Column (Box) Selection](#column-box-selection)
5. [🔍 Search & Replace](#-search--replace)
   - [Basic Search](#basic-search)
   - [Advanced Search](#advanced-search)
6. [🧠 Code Intelligence](#-code-intelligence)
   - [IntelliSense & Suggestions](#intellisense--suggestions)
   - [Navigation](#navigation)
   - [Symbol Navigation](#symbol-navigation)
7. [📱 Panel & View Management](#-panel--view-management)
   - [Sidebar & Panels](#sidebar--panels)
   - [Editor Layout](#editor-layout)
8. [📁 File Management](#-file-management)
   - [File Operations](#file-operations)
   - [File Navigation](#file-navigation)
9. [🖥️ Terminal](#️-terminal)
   - [Terminal Operations](#terminal-operations)
   - [Terminal Navigation](#terminal-navigation)
10. [🐛 Debug Operations](#-debug-operations)
    - [Debug Controls](#debug-controls)
11. [🎨 Display & UI](#-display--ui)
    - [Zoom & View](#zoom--view)
    - [Code Folding](#code-folding)
12. [🚀 Advanced Cursor Features](#-advanced-cursor-features)
    - [Composer Management](#composer-management)
    - [AI History & Context](#ai-history--context)
13. [📝 Markdown & Documentation](#-markdown--documentation)
    - [Markdown Preview](#markdown-preview)
14. [⚙️ Customization Tips](#️-customization-tips)
15. [🔧 Troubleshooting](#-troubleshooting)

- --

## 🤖 Cursor AI-Specific Features

> [!IMPORTANT]
> These are the core features that differentiate Cursor from standard VS Code. Mastering these will significantly boost your productivity.

### Essential AI Shortcuts

| Command                                     | Mac                     | Windows/Linux                    | Description                                              |
|---------------------------------------------|-------------------------|----------------------------------|----------------------------------------------------------|
| **Open Chat**                               | `⌘L`                    | `Ctrl+L`                         | Open AI chat interface                                   |
| **Open Composer**                           | `⌘I`                    | `Ctrl+I`                         | Open Cursor Composer (floating window)                   |
| **Open Full-screen Comp**                   | `⌘⇧I`                   | `Ctrl+Shift+I`                   | Open Composer in full-screen mode                        |
| **Inline Editing**                          | `⌘K`                    | `Ctrl+K`                         | Open inline AI editing                                   |
| **Toggle Agent**                            | `⌘.`                    | `Ctrl+.`                         | Switch between AI agents in Composer                     |
| **Toggle AI Models**                        | `⌘/`                    | `Ctrl+/`                         | Switch between available AI models                       |

### AI Code Completion (Cursor Tab)

| Command                                 | Mac                     | Windows/Linux                   | Description                                                 |
|-----------------------------------------|-------------------------|---------------------------------|-------------------------------------------------------------|
| **Accept Suggestion**                   | `Tab`                   | `Tab`                           | Accept AI code completion suggestion                        |
| **Reject Suggestion**                   | `Esc`                   | `Esc`                           | Reject AI suggestion                                        |
| **Partial Accept**                      | `⌘→`                    | `Ctrl+→`                        | Accept only the next word of a suggestion                   |

### AI Context & References

| Command                                     | Mac                        | Windows/Linux                    | Description                                               |
|---------------------------------------------|----------------------------|----------------------------------|-----------------------------------------------------------|
| **Add selection to Chat**                   | `⌘⇧L`                      | `Ctrl+Shift+L`                   | Add selected code to chat                                 |
| **Add selection to Edit**                   | `⌘⇧K`                      | `Ctrl+Shift+K`                   | Add selected code to edit                                 |
| **Submit with codebase**                    | `⌘Enter`                   | `Ctrl+Enter`                     | Send message with full codebase context                   |

### AI Inline Editing

| Command                                     | Mac                            | Windows/Linux                      | Description                                  |
|---------------------------------------------|--------------------------------|------------------------------------|----------------------------------------------|
| **Apply Changes**                           | `⌘Enter`                       | `Ctrl+Enter`                       | Apply AI suggested changes                   |
| **Cancel/Delete Changes**                   | `⌘Backspace`                   | `Ctrl+Backspace`                   | Cancel AI changes                            |

### AI @ Symbols (Context References)

| Symbol                            | Usage                                          | Description                                   |
|-----------------------------------|------------------------------------------------|-----------------------------------------------|
| `@filename`                       | `@package.json`                                | Reference specific file                       |
| `@functionName`                   | `@handleSubmit`                                | Reference specific function                   |
| `@variableName`                   | `@userState`                                   | Reference specific variable                   |
| `@codebase`                       | `@codebase query`                              | Search entire codebase                        |
| `@web`                            | `@web latest React patterns`                   | Search web for information                    |

- --

## 📂 General IDE Operations

### Command Palette & Settings

| Command                                       | Mac                            | Windows/Linux                           | Description                                      |
|-----------------------------------------------|--------------------------------|-----------------------------------------|--------------------------------------------------|
| **Show Command Palette**                      | `⌘⇧P` / `F1`                   | `Ctrl+Shift+P` / `F1`                   | Open command palette                             |
| **Quick Open (Go to File)**                   | `⌘P`                           | `Ctrl+P`                                | Quick file search                                |
| **User Settings**                             | `⌘,`                           | `Ctrl+,`                                | Open user settings                               |
| **Keyboard Shortcuts**                        | `⌘K ⌘S`                        | `Ctrl+K Ctrl+S`                         | Open keyboard shortcuts editor                   |
| **Cursor Settings**                           | `⌘⇧J`                          | `Ctrl+Shift+J`                          | Open Cursor-specific settings                    |

### Window Management

| Command                                     | Mac                      | Windows/Linux                    | Description                                           |
|---------------------------------------------|--------------------------|----------------------------------|-------------------------------------------------------|
| **New window/instance**                     | `⇧⌘N`                    | `Ctrl+Shift+N`                   | Create new project window                             |
| **Close window/instance**                   | `⌘W`                     | `Ctrl+W`                         | Close current window                                  |
| **Toggle full screen**                      | `⌃⌘F`                    | `F11`                            | Toggle fullscreen mode                                |
| **Zen Mode**                                | `⌘K Z`                   | `Ctrl+K Z`                       | Enter zen mode (Double Esc to exit)                   |

- --

## ✏️ Basic Editing

### Line Operations

| Command                                 | Mac                             | Windows/Linux                                   | Description                                     |
|-----------------------------------------|---------------------------------|-------------------------------------------------|-------------------------------------------------|
| **Cut line**                            | `⌘X`                            | `Ctrl+X`                                        | Cut current line                                |
| **Copy line**                           | `⌘C`                            | `Ctrl+C`                                        | Copy current line                               |
| **Delete line**                         | `⇧⌘K`                           | `Ctrl+Shift+K`                                  | Delete entire line                              |
| **Insert line below**                   | `⌘Enter`                        | `Ctrl+Enter`                                    | Insert new line below current                   |
| **Insert line above**                   | `⇧⌘Enter`                       | `Ctrl+Shift+Enter`                              | Insert new line above current                   |
| **Move line up/down**                   | `⌥↑` / `⌥↓`                     | `Alt+↑` / `Alt+↓`                               | Move current line up or down                    |
| **Copy line up/down**                   | `⇧⌥↑` / `⇧⌥↓`                   | `Shift+Alt+↑` / `Shift+Alt+↓`                   | Duplicate line up or down                       |

### Text Navigation

| Command                                        | Mac                              | Windows/Linux                              | Description                                  |
|------------------------------------------------|----------------------------------|--------------------------------------------|----------------------------------------------|
| **Go to start/end of line**                    | `Home` / `End`                   | `Home` / `End`                             | Navigate to line start/end                   |
| **Go to start/end of file**                    | `⌘↑` / `⌘↓`                      | `Ctrl+Home` / `Ctrl+End`                   | Navigate to file start/end                   |
| **Jump to matching bracket**                   | `⇧⌘\`                            | `Ctrl+Shift+\`                             | Jump to matching bracket                     |

### Indentation & Formatting

| Command                                   | Mac                           | Windows/Linux                         | Description                                     |
|-------------------------------------------|-------------------------------|---------------------------------------|-------------------------------------------------|
| **Indent/outdent line**                   | `⌘]` / `⌘[`                   | `Ctrl+]` / `Ctrl+[`                   | Increase/decrease indentation                   |
| **Format document**                       | `⇧⌥F`                         | `Shift+Alt+F`                         | Format entire document                          |
| **Format selection**                      | `⌘K ⌘F`                       | `Ctrl+K Ctrl+F`                       | Format selected text                            |

### Comments

| Command                                    | Mac                       | Windows/Linux                     | Description                            |
|--------------------------------------------|---------------------------|-----------------------------------|----------------------------------------|
| **Toggle line comment**                    | `⌘/`                      | `Ctrl+/`                          | Toggle line comment                    |
| **Toggle block comment**                   | `⇧⌥A`                     | `Shift+Alt+A`                     | Toggle block comment                   |
| **Add line comment**                       | `⌘K ⌘C`                   | `Ctrl+K Ctrl+C`                   | Add line comment                       |
| **Remove line comment**                    | `⌘K ⌘U`                   | `Ctrl+K Ctrl+U`                   | Remove line comment                    |

- --

## 🎯 Multi-Cursor & Selection

### Multi-Cursor Operations

| Command                                         | Mac                             | Windows/Linux                                 | Description                                               |
|-------------------------------------------------|---------------------------------|-----------------------------------------------|-----------------------------------------------------------|
| **Insert cursor**                               | `⌥ + click`                     | `Alt + click`                                 | Add cursor at specific position                           |
| **Insert cursor above/below**                   | `⌥⌘↑` / `⌥⌘↓`                   | `Ctrl+Alt+↑` / `Ctrl+Alt+↓`                   | Add cursor vertically                                     |
| **Undo last cursor action**                     | `⌘U`                            | `Ctrl+U`                                      | Undo last cursor operation                                |
| **Cursor at end of lines**                      | `⇧⌥I`                           | `Shift+Alt+I`                                 | Add cursor at end of each selected line                   |

### Text Selection

| Command                                       | Mac                               | Windows/Linux                                   | Description                                                 |
|-----------------------------------------------|-----------------------------------|-------------------------------------------------|-------------------------------------------------------------|
| **Select current line**                       | `⌘L`                              | `Ctrl+L`                                        | Select entire line                                          |
| **Select all occurrences**                    | `⇧⌘L`                             | `Ctrl+Shift+L`                                  | Select all instances of current selection                   |
| **Select all word matches**                   | `⌘F2`                             | `Ctrl+F2`                                       | Select all instances of current word                        |
| **Add next match to sel**                     | `⌘D`                              | `Ctrl+D`                                        | Add next occurrence of selection                            |
| **Expand/shrink selection**                   | `⌃⇧⌘→` / `⌃⇧⌘←`                   | `Shift+Alt+→` / `Shift+Alt+←`                   | Smart selection logic                                       |

### Column (Box) Selection

| Command                                        | Mac                               | Windows/Linux                          | Description                                          |
|------------------------------------------------|-----------------------------------|----------------------------------------|------------------------------------------------------|
| **Column selection mouse**                     | `⇧⌥ + drag`                       | `Shift+Alt + drag`                     | Select text in columns using mouse                   |
| **Column selection up/down**                   | `⇧⌥⌘↑` / `⇧⌥⌘↓`                   | `Ctrl+Shift+Alt+↑/↓`                   | Selection up/down                                    |
| **Column selection side**                      | `⇧⌥⌘←` / `⇧⌥⌘→`                   | `Ctrl+Shift+Alt+←/→`                   | Selection left/right                                 |

- --

## 🔍 Search & Replace

### Basic Search

| Command                                  | Mac                            | Windows/Linux                       | Description                                |
|------------------------------------------|--------------------------------|-------------------------------------|--------------------------------------------|
| **Find**                                 | `⌘F`                           | `Ctrl+F`                            | Open find dialog                           |
| **Find next/previous**                   | `⌘G` / `⇧⌘G`                   | `F3` / `Shift+F3`                   | Find next/previous match                   |
| **Replace**                              | `⌥⌘F`                          | `Ctrl+H`                            | Open replace dialog                        |
| **Replace in files**                     | `⇧⌘H`                          | `Ctrl+Shift+H`                      | Global find and replace                    |

### Advanced Search

| Command                                  | Mac                        | Windows/Linux                     | Description                                                 |
|------------------------------------------|----------------------------|-----------------------------------|-------------------------------------------------------------|
| **Show Search panel**                    | `⇧⌘F`                      | `Ctrl+Shift+F`                    | Open global search panel                                    |
| **Select all matches**                   | `⌥Enter`                   | `Alt+Enter`                       | Select all search matches                                   |
| **Skip and find next**                   | `⌘K ⌘D`                    | `Ctrl+K Ctrl+D`                   | Move to next match without adding current                   |

- --

## 🧠 Code Intelligence

### IntelliSense & Suggestions

| Command                                       | Mac                         | Windows/Linux                        | Description                                     |
|-----------------------------------------------|-----------------------------|--------------------------------------|-------------------------------------------------|
| **Trigger suggestion**                        | `⌃Space`                    | `Ctrl+Space`                         | Manually trigger IntelliSense                   |
| **Trigger parameter hints**                   | `⇧⌘Space`                   | `Ctrl+Shift+Space`                   | Show parameter types/names                      |
| **Quick Fix**                                 | `⌘.`                        | `Ctrl+.`                             | Show available quick fixes                      |

### Navigation

| Command                                  | Mac                        | Windows/Linux                   | Description                                           |
|------------------------------------------|----------------------------|---------------------------------|-------------------------------------------------------|
| **Go to Definition**                     | `F12`                      | `F12`                           | Jump to definition of symbol                          |
| **Peek Definition**                      | `⌥F12`                     | `Alt+F12`                       | Peek definition inline                                |
| **Definition to side**                   | `⌘K F12`                   | `Ctrl+K F12`                    | Open definition in split editor                       |
| **Go to References**                     | `⇧F12`                     | `Shift+F12`                     | Show all symbol references                            |
| **Rename Symbol**                        | `F2`                       | `F2`                            | Rename symbol across entire project                   |

### Symbol Navigation

| Command                                    | Mac                     | Windows/Linux                    | Description                                        |
|--------------------------------------------|-------------------------|----------------------------------|----------------------------------------------------|
| **Show all Symbols**                       | `⌘T`                    | `Ctrl+T`                         | Search symbols globally                            |
| **Go to Symbol in file**                   | `⇧⌘O`                   | `Ctrl+Shift+O`                   | Navigate symbols in current file                   |
| **Go to Line**                             | `⌃G`                    | `Ctrl+G`                         | Jump to specific line number                       |

- --

## 📱 Panel & View Management

### Sidebar & Panels

| Command                                   | Mac                     | Windows/Linux                    | Description                                      |
|-------------------------------------------|-------------------------|----------------------------------|--------------------------------------------------|
| **Toggle Sidebar**                        | `⌘B`                    | `Ctrl+B`                         | Show or hide sidebar                             |
| **Show Explorer**                         | `⇧⌘E`                   | `Ctrl+Shift+E`                   | Open file explorer                               |
| **Show Source Control**                   | `⌃⇧G`                   | `Ctrl+Shift+G`                   | Open Git/version control panel                   |
| **Show Debug**                            | `⇧⌘D`                   | `Ctrl+Shift+D`                   | Open debug panel                                 |
| **Show Extensions**                       | `⇧⌘X`                   | `Ctrl+Shift+X`                   | Open extensions search                           |
| **Show Problems**                         | `⇧⌘M`                   | `Ctrl+Shift+M`                   | View errors and warnings                         |
| **Show Output**                           | `⇧⌘U`                   | `Ctrl+Shift+U`                   | View output channels                             |

### Editor Layout

| Command                                   | Mac                            | Windows/Linux                         | Description                                                |
|-------------------------------------------|--------------------------------|---------------------------------------|------------------------------------------------------------|
| **Split editor**                          | `⌘\`                           | `Ctrl+\`                              | Split current editor vertically                            |
| **Toggle layout**                         | `⌥⌘0`                          | `Shift+Alt+0`                         | Toggle between vertical/horizontal split                   |
| **Focus editor groups**                   | `⌘1`/`2`/`3`                   | `Ctrl+1`/`2`/`3`                      | Focus specific split group                                 |
| **Navigate groups**                       | `⌘K ⌘←`/`→`                    | `Ctrl+K Ctrl+←`/`→`                   | Move between split windows                                 |

- --

## 📁 File Management

### File Operations

| Command                                    | Mac                       | Windows/Linux                     | Description                                    |
|--------------------------------------------|---------------------------|-----------------------------------|------------------------------------------------|
| **New File**                               | `⌘N`                      | `Ctrl+N`                          | Create new file                                |
| **Open File**                              | `⌘O`                      | `Ctrl+O`                          | Open file picker                               |
| **Save File**                              | `⌘S`                      | `Ctrl+S`                          | Save current editor                            |
| **Save As**                                | `⇧⌘S`                     | `Ctrl+Shift+S`                    | Save with new name                             |
| **Save All**                               | `⌥⌘S`                     | `Ctrl+K S`                        | Save all modified files                        |
| **Close editor**                           | `⌘W`                      | `Ctrl+W`                          | Close current tab                              |
| **Close All editors**                      | `⌘K ⌘W`                   | `Ctrl+K Ctrl+W`                   | Close all open tabs                            |
| **Reopen closed editor**                   | `⇧⌘T`                     | `Ctrl+Shift+T`                    | Restore recently closed file                   |

### File Navigation

| Command                                  | Mac                      | Windows/Linux                   | Description                                         |
|------------------------------------------|--------------------------|---------------------------------|-----------------------------------------------------|
| **Copy file path**                       | `⌘K P`                   | `Ctrl+K P`                      | Copy path of active file                            |
| **Reveal in Explorer**                   | `⌘K R`                   | `Ctrl+K R`                      | Show file in system file explorer                   |
| **Open in new window**                   | `⌘K O`                   | `Ctrl+K O`                      | Open current file in a new window                   |

- --

## 🖥️ Terminal

### Terminal Operations

| Command                                   | Mac                        | Windows/Linux                    | Description                                             |
|-------------------------------------------|----------------------------|----------------------------------|---------------------------------------------------------|
| **Show Terminal**                         | `⌃``                       | `Ctrl+``                         | Toggle integrated terminal panel                        |
| **Create new terminal**                   | `⌃⇧``                      | `Ctrl+Shift+``                   | Open new terminal instance                              |
| **AI Command Gen**                        | `⌘K`                       | `Ctrl+K`                         | Generate terminal commands with AI                      |
| **Run generated cmd**                     | `⌘Enter`                   | `Ctrl+Enter`                     | Execute AI suggested terminal command                   |
| **Accept suggestion**                     | `Esc`                      | `Esc`                            | Accept AI suggestion without running                    |

### Terminal Navigation

| Command                                     | Mac                                | Windows/Linux                              | Description                                   |
|---------------------------------------------|------------------------------------|--------------------------------------------|-----------------------------------------------|
| **Scroll output**                           | `⌘↑` / `⌘↓`                        | `Ctrl+↑` / `Ctrl+↓`                        | Scroll terminal history                       |
| **Page Up / Down**                          | `PgUp`/`PgDn`                      | `PgUp`/`PgDn`                              | Jump through terminal pages                   |
| **Scroll to extremities**                   | `⌘Home` / `⌘End`                   | `Ctrl+Home` / `Ctrl+End`                   | Jump to terminal start/end                    |

- --

## 🐛 Debug Operations

### Debug Controls

| Command                                 | Mac                       | Windows/Linux                     | Description                                                |
|-----------------------------------------|---------------------------|-----------------------------------|------------------------------------------------------------|
| **Toggle breakpoint**                   | `F9`                      | `F9`                              | Add/remove line breakpoint                                 |
| **Start/Continue**                      | `F5`                      | `F5`                              | Start or resume debug execution                            |
| **Step Into**                           | `F11`                     | `F11`                             | Enter into current function call                           |
| **Step Out**                            | `⇧F11`                    | `Shift+F11`                       | Finish current function and return                         |
| **Step Over**                           | `F10`                     | `F10`                             | Execute next line without entering funcs                   |
| **Stop debugging**                      | `⇧F5`                     | `Shift+F5`                        | Terminate debug session                                    |
| **Show hover info**                     | `⌘K ⌘I`                   | `Ctrl+K Ctrl+I`                   | Show variable value in tooltip                             |

- --

## 🎨 Display & UI

### Zoom & View

| Command                                | Mac                            | Windows/Linux                         | Description                                                 |
|----------------------------------------|--------------------------------|---------------------------------------|-------------------------------------------------------------|
| **Zoom in/out**                        | `⌘=` / `⇧⌘-`                   | `Ctrl+=` / `Ctrl+-`                   | Adjust global UI zoom level                                 |
| **Toggle word wrap**                   | `⌥Z`                           | `Alt+Z`                               | Wrap long lines of code                                     |
| **Toggle minimap**                     | N/A                            | N/A                                   | Toggle code minimap (via Command Palette)                   |

### Code Folding

| Command                                      | Mac                              | Windows/Linux                           | Description                                 |
|----------------------------------------------|----------------------------------|-----------------------------------------|---------------------------------------------|
| **Fold/unfold region**                       | `⌥⌘[` / `⌥⌘]`                    | `Ctrl+Shift+[` / `]`                    | Fold current code block                     |
| **Fold/unfold subregions**                   | `⌘K ⌘[` / `⌘]`                   | `Ctrl+K Ctrl+[` / `]`                   | Fold all nested blocks                      |
| **Fold/unfold ALL**                          | `⌘K ⌘0` / `⌘J`                   | `Ctrl+K Ctrl+0` / `J`                   | Fold or unfold everything                   |

- --

## 🚀 Advanced Cursor Features

### Composer Management

| Command                                  | Mac                           | Windows/Linux                         | Description                                        |
|------------------------------------------|-------------------------------|---------------------------------------|----------------------------------------------------|
| **Start new composer**                   | `⌘N` / `⌘R`                   | `Ctrl+N` / `Ctrl+R`                   | Create a fresh composer session                    |
| **Close composer**                       | `⌘W`                          | `Ctrl+W`                              | Close the composer interface                       |
| **Composer bar mode**                    | `⌘⇧K`                         | `Ctrl+Shift+K`                        | Switch composer to bar layout                      |
| **Composer History**                     | `⌘[` / `⌘]`                   | `Ctrl+[` / `Ctrl+]`                   | Navigate through session history                   |

### AI History & Context

| Command                                  | Mac                        | Windows/Linux                    | Description                                             |
|------------------------------------------|----------------------------|----------------------------------|---------------------------------------------------------|
| **Activity History**                     | `⌘⌥L`                      | `Ctrl+Alt+L`                     | Open global AI interaction history                      |
| **Toggle Input Focus**                   | `⌘⇧K`                      | `Ctrl+Shift+K`                   | Quickly focus on the AI input field                     |
| **Ask quick question**                   | `⌥Enter`                   | `Alt+Enter`                      | Trigger immediate quick query                           |
| **Context Strategy**                     | `⌘M`                       | `Ctrl+M`                         | Cycle through file reading strategies                   |

- --

## 📝 Markdown & Documentation

### Markdown Preview

| Command                               | Mac                      | Windows/Linux                    | Description                                      |
|---------------------------------------|--------------------------|----------------------------------|--------------------------------------------------|
| **Open Preview**                      | `⇧⌘V`                    | `Ctrl+Shift+V`                   | Toggle Markdown preview mode                     |
| **Preview to side**                   | `⌘K V`                   | `Ctrl+K V`                       | Open preview in a split window                   |

- --

## ⚙️ Customization Tips

1. **Open keyboard shortcuts editor**: `⌘K ⌘S` (Mac) / `Ctrl+K Ctrl+S` (Windows)
2. **Search for specific commands**: Use the search bar for "Cursor" or "AI".
3. **Pencil icon**: Click to modify or assign new keys.
4. **JSON Mode**: Ideal for advanced users to sync or copy keybindings across machines.

- --

## 🔧 Troubleshooting

- **Conflicting Shortcuts**: Some system keys (especially Windows) might override IDE hotkeys.
- **Unresponsive AI**: Check your Cursor login status and model configuration.
- **Context not loading**: Ensure you are in a Workspace and the index is up-to-date.
- **Custom Bindings Ignored**: Double-check `keybindings.json` for syntax errors.

- --

_Last updated: February 2026_
_Sources: Cursor101, Starmorph Blog, Mehmet Baykar, Cursor Community Forum_
