# bootstrap

## 让表格呈现出滚动条

在 table 外加一层 div,div 添加 table-responsive 类，table 上添加 text-nowrap 类

```js
<div className='table-responsive'>
  <table className='table text-nowrap'>
    <thead>
      <tr>...</tr>
    </thead>
    <tbody>...</tbody>
  </table>
</div>
```

## 让表格单元格自动换行

以下为让文件名单元格自动换行

```js
<table className='table' style={{ textAlign: 'center', wordBreak: 'break-all', wordWrap: 'break-all' }}>
  <thead>
    <tr className='active' style={{ fontWeight: 'bold' }}>
      <td>编号</td>
      <td width='20%'>文件名</td>
      ......
    </tr>
  </thead>
  ....
</table>
```
