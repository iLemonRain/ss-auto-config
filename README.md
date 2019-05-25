# ss-auto-config
自动抓取网上发布的SS免费账号信息, 并生成 `gui-config.json`. 配合 [ss-qt5](https://github.com/shadowsocks/shadowsocks-qt5) 使用, 可以无痛科学上网

## 原理
网上会有免费的服务器发布, 只不过为了防爬虫, 服务器信息会以图片的形式提供, 而且服务器信息会定期更换, 每次更换后都要手动打开浏览器查一下新的信息, 然后修改 ss-qt5 的配置, 很麻烦

这份代码可以爬取并识别出服务器信息, 然后为 ss-qt5 生成配置文件 `gui-config.json`, 解放双手

## 使用方法

### Linux

1. 安装OCR引擎和中文语言包
```bash
sudo apt update
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-chi-sim
```

2. 下载 [ss-qt5 release](https://github.com/shadowsocks/shadowsocks-qt5/releases)

```bash
sudo ln -s /absolute/path/to/your/AppImage /usr/local/bin/ss-start
```

3. clone 代码
```bash
git clone https://github.com/slimwang/ss-auto-config.git
cd ss-auto-config
pipenv install
```

4. 执行
```bash
chmod +x app.py
./app.py
```
或者
```bash
python app.py
```
输出:
```bash
正在抓取免费账号图片...
免费账号图片抓取完成
正在识别图片中的文本...
文本识别完成
正在生成服务器列表...
服务器列表生成完毕
[   
    {   
        'method': 'method',
        'password': 'password',
        'remarks': 'server1',
        'server': 'ip',
        'server_port': 12345
    },
    {   
        'method': 'method',
        'password': 'password',
        'remarks': '2',
        'server': '6ip',
        'server_port': 54321
    }
]
正在生成配置文件...
`gui-config.json` 已生成
```

5. 打开 ss-qt5 AppImage, 导入生成的 `gui-config.json`  
ss-qt5没有命令行接口, 需要手动导入 `gui-config.json`

### Win

Windows 用户不需要科学上网

## Question
* 为什么不用原生的 ss, 而是用 ss-qt5?  
ss 已经被原作者废弃了, 代码不再更新了. 如果用的话, 需要自己手动修复 bug  
如: oppen-ssl 在新版本中废弃了 CLEAN_UP 函数, 需要自己去改 ss 代码, 将其`openssl.py` 中的相应函数修改为新的 reset 函数, 很麻烦.
* 为什么不管 windows 用户?  
服务器ip 端口 密码 加密协议 这些都有, win用户可以自己去找个 ss 客户端, 然后填写这些信息即可
