# Web-Spider-Service

A simple web spider service based in HTTP, capturing information in Taobao, Tianmao, Jingdong, Dangdang, Suning and Today's Focus news.

><br/>***Unique Studio Hackweek project***<br/><br/>
***XiaoDu, a funny chat robot equiped with shopping web-spider, which has three mode to choose.***<br/>
***Android Client: @ Enble DU***<br/>
***Backstage: @ yukiiris***<br/>
***Design: @ Zhu Li***<br/>
***Spider Service: @ Yue Pan***<br/>
***Development Language: JAVA, Python***<br/>
***Platform: QQ for Android and IOS***<br/>
***Attribute Set Platform: Android***<br/>
***Finish day: 2017.8.3***

GitHub for Andriod: [HackWeekProjectAndroid](https://github.com/D384509085/HackWeekProjectAndroid)

GitHub for Entity: [HackWeekProjectEntity](https://github.com/D384509085/HackWeekProjectAndroid)

GitHub for Backstage: [XiaoDu](https://github.com/yukiiris/XiaoDu)

## Features

### Port

Default port: 8080

You can set port in `Web-Server.py line:109`

### URL 

`your-server-address:8080/mode + key`

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