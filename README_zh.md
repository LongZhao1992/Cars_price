
# 车辆数据获取器

## 描述

这个脚本 `fetch_vehicles.py` 旨在从指定的网页抓取车辆信息，并将数据保存为CSV格式。它可以捕获如车辆的标题、年份、里程和价格等详细信息。对于希望从特定在线源编译车辆列表到一个易于管理的格式的人来说，这个工具非常有用。目前只测试过cars.com[https://www.cars.com/].

## 功能

- 获取车辆详情，包括标题、年份、里程和价格
- 以CSV格式输出数据，便于分析和处理
- 命令行界面，使用直接

## 安装

在运行脚本之前，请确保您的系统上安装了Python。这个脚本是考虑到Python 3.x版本开发的。

您还需要安装以下Python包：`requests` 和 `beautifulsoup4`。您可以使用pip安装这些包：

```bash
pip install requests beautifulsoup4
```

## 使用

要使用脚本，请导航到 `fetch_vehicles.py` 所在的目录，并在终端中运行以下命令：

```bash
python fetch_vehicles.py [URL] [输出CSV文件名]
```

将 `[URL]` 替换为您希望从中抓取车辆数据的目标网页URL，将 `[输出CSV文件名]` 替换为您希望的输出CSV文件的名称。

### 示例

```bash
python fetch_vehicles.py "http://example.com/vehicles" "vehicles.csv"
```

此命令从 `http://example.com/vehicles` 抓取车辆数据，并将其保存到 `vehicles.csv`。

## 参数

- `URL`: 包含车辆列表的目标网页URL。
- `输出CSV文件名`: 数据将被保存的输出CSV文件的名称。

## 贡献

如果您想为这个项目做出贡献，请随意fork仓库，进行更改，并提交pull请求。我们非常感谢您的贡献！

## 许可证

该项目是开源的，可在 [MIT 许可证](LICENSE) 下获得。
