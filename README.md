# Web-Spider-Service

A simple web spider service based in HTTP, capturing information in Taobao, Tianmao, Jingdong, Dangdang, Suning and Today's Focus news.

***Unique Studio Hackweek project***

***XiaoDu, a funny chat robot equiped with shopping web-spider, which has three mode to choose.***

***Android Client: @ Enble DU***

***Backstage: @ yukiiris***

***Design: @ Zhu Li***

***Spider Service: @ Yue Pan***

***Development Language: JAVA, Python***

***Platform: QQ for Android and IOS***

***Attribute Set Platform: Android***

***Finish day: 2017.8.3***

GitHub for Andriod: [HackWeekProjectAndroid](https://github.com/D384509085/HackWeekProjectAndroid)

GitHub for Entity: [HackWeekProjectEntity](https://github.com/D384509085/HackWeekProjectAndroid)

GitHub for Backstage: [XiaoDu](https://github.com/yukiiris/XiaoDu)

## Features

### Default port: 8080

You can set port in `Web-Server.py line: `

### URL: `your-server-address:8080/mode + key`

you can deploy the server in your machine, and when it receive a HTTP GET request, then it will analyze the url and start spider.

### REPLY 

The service will reply a json include all information it get, the separator is `'#'`

Then you can analyze the reply json and send the information to client.

## Thanks

Thanks Zhu Li for designing the UI.

Thanks Du Enbo for Writting Android Client.

Thanks Bao Rong for Writting backstage.

Thanks our effort in 2017 Unique Studio Summer Camp Hackweek.

Thanks our child Xiaodu.

### Copyright 2017 @ Zhu Li, Du Enbo, Bao Rong, Pan Yue