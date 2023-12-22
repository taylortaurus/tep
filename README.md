框架教程：https://gitee.com/dongfanger/tep/wikis

🌟更新日志🌟
- ✅V2.2.3
  - case文件夹下使用中文命名，目录名+模块名（包名+模块名）
  - 修改pytest配置python_files = *.py，识别任意名称
  - 脚手架添加中文命名示例
  - 脚手架添加场景测试用例
  - 脚手架添加Mock服务工具
  - 脚手架添加fixture\fixture_login.py
  - requests日志耗时改为毫秒
- V2.2.2
  - 基于Python12.1版本，poetry update
  - 移除allure报告，去掉--tep-reports命令行参数
  - 定制pytest-html报告内容和样式，单个HTML文件查看报告
- V2.2.1
  - 新增关键字StringKeyword，url使用`${}`替换变量
  - 回放配置添加hookVar，可自定义变量池
  - 回放配置添加hookUrl，可自定义url
  - 回放配置添加hookHeaders，可自定义headers
  - 修复BUG，回放对比生成HTML，删除顶部多余td
- V2.2.0
  - 重要：BodyKeyword改名为JSONKeyword
  - 重要：headers和body均为String，多行字符串表示，用JSONKeyword转为dict
  - 重要：新增关键字VarKeyword，与JSONKeyword结合使用，实现`${}`用法，在字符串中直接替换变量
  - 重要：去掉Result类，无须指定返回类型和定义中间变量，让关键字返回动态起来
  - 抓包自动生成用例，配置新增jsonIndent，默认设置为4，换行且4个空格缩进，可设置None不换行
  - 抓包自动生成用例，配置mode改名为overwrite，默认跳过，True则覆盖
  - 抓包自动生成用例，根据新特性，优化模版代码
- V2.1.2
  - 优化Har，支持指定目录，按增量/全量转换pytest用例
- V2.1.1
  - HAR包转换pytest用例功能纳入脚手架，主推，内容写入教程“快速入门”章节
  - 脚手架.gitignore文件后缀问题修复
- V2.1.0
  - 支持HTTP/2协议，httpx库实现
  - 支持HAR包转换为pytest用例，支持HTTP1和HTTP2协议
  - 基于HAR包的回放对比，字段对比输出TXT，文本对比输出HTML
  - 自定义日志对象，logger和sys_logger输出到用户/系统不同文件
  - 支持接口重试，CODE码/异常匹配，超时设置等，tenacity库实现
- V2.0.1 cli修改，查看版本`tep -V`，V大写，创建脚手架`tep new demo`，使用new
- V2.0.0 tep关键字驱动框架
- V1.0.0 tep小工具完整教程
- V0.2.3 tep小工具首次开源