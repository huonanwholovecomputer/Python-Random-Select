## Python随机抽取（PY单文件）

提供了一个可用的Python随机抽取（PY单文件）

需要注意的是，对于all版本，"**keyboard**"模块不是Python自带的，

所以，需要使用终端（CMD、PowerShell等）运行以下命令进行安装：

```
pip install keyboard
```
而在windows版本中，我使用了`msvcrt`模块替换了`keyboard`模块。

`msvcrt`模块在Windows系统中拥有更大的优势，而`keyboard`模块拥有更好的跨平台兼容性。

## 如何将Python程序打包成exe文件？

### 假设

  1.我们假设需要包装的Python脚本位置在`C:\Users\Administrator\Downloads\`
  
  2.我们假设需要包装的Python脚本名为`随机抽取v1.0.build-77.9.1-windows.PY`

### 方法

  使用Python的`PyInstaller`模块。这是一个非常流行和方便的工具，能够将Python脚本转换为独立的可执行文件(exe)。

### 具体步骤：

1. **安装 PyInstaller**:

    打开命令提示符并输入以下命令安装 `PyInstaller`：
   ```
   pip install pyinstaller
   ```

2. **导航到 Python 脚本所在的目录**:

    使用命令提示符导航到需要包装的Python脚本所在的目录，比如： `C:\Users\Administrator\Downloads\`。

   ```
   cd C:\Users\Administrator\Downloads
   ```

3. **使用 PyInstaller 打包 Python 脚本**:

    使用以下命令将Python脚本打包成exe文件：
   ```
   pyinstaller --onefile "随机抽取v1.0.build-77.9.1-windows.PY"
   ```
    这个命令将创建一个独立的可执行文件。`--onefile` 参数指定将所有内容打包成一个单独的可执行文件。

4. **查找生成的 exe 文件**:

    PyInstaller 完成后，会在当前目录下生成一个 `dist` 文件夹，里面包含生成的 exe 文件。路径如下：
   ```
   C:\Users\Administrator\Downloads\dist\随机抽取v1.0.build-77.9.1-windows.exe
   ```

### 注意事项

- **路径和文件名**：确保你的Python脚本路径和文件名正确无误。如果脚本路径或文件名包含空格或特殊字符，建议使用引号将其括起来（如上面的示例所示）。
- **依赖包**：确保所有的依赖包都已安装，并且在打包之前可以正常运行脚本。
- **图标和其他资源**：如果你想为生成的exe文件指定图标，可以使用 `--icon` 参数。例如：
  ```
  pyinstaller --onefile --icon=youricon.ico "随机抽取v1.0.build-77.9.1-windows.PY"
  ```

通过上述步骤，你就可以将Python脚本成功打包为exe文件。
