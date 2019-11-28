# 工具函数

## 千分符

```js
function format(num) {
  let arr = [];
  let str = '' + num;
  let intPart = '';
  let digitPart = '';
  let count = '';
  if (str.indexOf('.') !== -1) {
    intPart = str.split('.')[0];
    digitPart = str.split('.')[1];
  } else {
    intPart = str;
  }

  count = intPart.length;

  while (count >= 3) {
    arr.unshift(intPart.slice(count - 3, count));
    count -= 3;
  }

  // 如果是不是3的倍数就另外追加到上去
  intPart.length % 3 && arr.unshift(intPart.slice(0, intPart.length % 3));

  if (digitPart.length > 0) {
    return `${arr.toString()}.${digitPart}`;
  } else {
    return arr.toString();
  }
}
console.log(format(12345678.12));
```

## 时间戳转日期

```js
/**
 * 将小于10的值加上零
 * @param {number} value 数字
 * @return {string}
 */
function formatNumber(value) {
  return `${value < 10 ? '0' + value : value}`;
}

**
 * 时间戳转日期
 * @param {number} timestamp 时间戳
 * @return 日期，格式为2019-06-03 10:16:09
 */
function timeStampToTime(timestamp) {
  timestamp = timestamp.toString().length == 10 ? timestamp * 1000 : timestamp;
  const date = new Date(timestamp);
  const year = date.getFullYear();
  const month = date.getMonth() + 1;
  const day = date.getDate();
  const hour = date.getHours();
  const minute = date.getMinutes();
  const second = date.getSeconds();
  return `${year}-${formatNumber(month)}-${formatNumber(day)} ${formatNumber(hour)}:${formatNumber(
    minute
  )}:${formatNumber(second)}`;
}
```

## 日期转时间戳

```js
/**
 * 日期转时间戳
 * @param {string} time 日期格式
 * @param {boolean} isUnix 是否是unix格式(10位)
 * @return {number} 时间戳
 */
function timeToTimeStamp(time, isUnix) {
  const date = new Date(time);
  const timestamp = date.getTime();
  return isUnix ? timestamp / 1000 : timestamp;
}
```

## 是否是11位有效手机号

```js
/**
 * 判断是否是11位有效手机号
 * @param {number} phoneNum 手机号
 */
function isValidPhone(phoneNum) {
  const phoneReg = /^[1][3,4,5,7,8][0-9]{9}$/;
  if (!phoneReg.test(phoneNum)) {
    return false;
  } else {
    return true;
  }
}
```