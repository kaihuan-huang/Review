### 第一题：Conference Schedule

#### 题目描述：
给定一组会议的开始和结束时间，要求计算一个人能够参加的最大会议数量，要求会议不能重叠。

#### 原理：
这道题目可以使用贪心算法。我们优先选择结束时间最早的会议，这样能够给后面的会议留出更多的时间，从而参加更多的会议。

#### 解决方案（Python）：

```python
def maxPresentations(scheduleStart, scheduleEnd):
    # 将开始时间和结束时间配对
    presentations = sorted(zip(scheduleStart, scheduleEnd), key=lambda x: x[1])
    
    max_presentations = 0
    last_end_time = 0
    
    for start, end in presentations:
        if start >= last_end_time:
            max_presentations += 1
            last_end_time = end
    
    return max_presentations
```

#### 主要步骤：
1. 将会议的开始时间和结束时间配对，并按照结束时间排序。
2. 遍历排序后的会议，选择那些开始时间不早于上一次会议结束时间的会议。
3. 统计可以参加的会议数量。

---

### 第二题：Youngest Employees

#### 题目描述：
从两个表 `EMPLOYEE` 和 `EMPLOYEE_UIN` 中，查询出年龄小于25岁的员工，并按名字（字母序）和ID（数字序）排序。输出应包括 `UIN` 和 `NAME`。

#### 原理：
首先通过 `ID` 将两个表进行连接，然后根据条件筛选出符合条件的员工，最后按照要求排序并输出。

#### 解决方案（SQL）：

```sql
SELECT E_U.UIN, E.NAME
FROM EMPLOYEE E
INNER JOIN EMPLOYEE_UIN E_U ON E.ID = E_U.ID
WHERE E.AGE < 25
ORDER BY E.NAME ASC, E.ID ASC;
```

#### 主要步骤：
1. 使用 `INNER JOIN` 将两个表按 `ID` 连接。
2. 使用 `WHERE` 过滤年龄小于25岁的员工。
3. 使用 `ORDER BY` 对结果按 `NAME` 和 `ID` 进行排序。
4. 选择 `UIN` 和 `NAME` 输出。

---

### 第三题：REST API - 获取患者的平均体温

#### 题目描述：
给定一个用户ID，通过API获取该用户的所有医疗记录，并计算其平均体温。API支持分页，需要遍历所有页面。

#### 原理：
使用Python的`requests`库进行API调用，逐页获取数据并累计体温数据。处理完成后计算平均体温，若无记录则返回 `"0"`。

#### 解决方案（Python）：

```python
import requests

def getAverageTemperatureForUser(userId):
    base_url = f"https://jsonmock.hackerrank.com/api/medical_records?userId={userId}&page="
    
    # 初始化变量
    total_temperature = 0.0
    record_count = 0
    page = 1
    
    while True:
        # 获取当前页面数据
        response = requests.get(base_url + str(page))
        data = response.json()
        
        # 如果没有数据，退出循环
        if len(data['data']) == 0:
            break
        
        # 处理每条记录以累计体温
        for record in data['data']:
            if 'vitals' in record and 'bodyTemperature' in record['vitals']:
                total_temperature += record['vitals']['bodyTemperature']
                record_count += 1
        
        # 检查是否为最后一页
        if page >= data['total_pages']:
            break
        
        # 进入下一页
        page += 1
    
    # 返回平均体温，格式化为一位小数
    if record_count > 0:
        average_temperature = total_temperature / record_count
        return f"{average_temperature:.1f}"
    else:
        return "0"

if __name__ == '__main__':
    userId = int(input().strip())
    result = getAverageTemperatureForUser(userId)
    print(result)
```

#### 主要步骤：
1. 使用`requests.get`方法获取指定页面的数据。
2. 遍历每个页面的所有记录，累计体温值并计数。
3. 处理完所有页面后，计算并返回平均体温（若无记录则返回 `"0"`）。
4. 格式化输出结果，使其保留一位小数。

通过这些步骤，这三道题都能够高效地解决。每道题都运用了相应的算法和数据处理技巧，确保结果的准确性和性能的优化。

'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding("ascii");
let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (chunk) {
    inputString += chunk;
});
process.stdin.on("end", function () {
    inputString = inputString.split('\n');
    main();
});

function readLine() {
  return inputString[currentLine++];
}

class Size {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
}

class Image {
    constructor(url, size) {
        this.url = url;
        this.size = size;
    }

    getUrl() {
        return this.url;
    }

    setUrl(url) {
        this.url = url;
    }

    getSize() {
        return this.size;
    }

    setSize(width, height) {
        this.size.width = width;
        this.size.height = height;
    }

    cloneImage() {
        return new Image(this.url, new Size(this.size.width, this.size.height));
    }
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    
    let images = [];
    
    let numberOfImages = parseInt(readLine().trim());
    
    while (numberOfImages-- > 0) {
        let inputs = readLine().trim().split(' ');
        images.push(new Image(inputs[0], new Size(parseInt(inputs[1]), parseInt(inputs[2]))));
    }

    let numberOfOperations = parseInt(readLine().trim());
    while (numberOfOperations-- > 0) {
        let inputs = readLine().trim().split(' ');
        const image = images[parseInt(inputs[1]) - 1];
        const operation = inputs[0];
        
        switch(operation) {
            case 'Clone':
                images.push(image.cloneImage());
                break;
            case 'UpdateUrl':
                image.setUrl(inputs[2]);
                break;
            case 'UpdateSize':
                image.setSize(parseInt(inputs[2]), parseInt(inputs[3]));
                break;
            default:
                break;
        }
    }
    
    images.forEach((img) => {
        const size = img.getSize();
        ws.write(`${img.getUrl()} ${size.width} ${size.height}\n`);
    })
}
