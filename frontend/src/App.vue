<script setup>
import 'bootstrap-icons/font/bootstrap-icons.css'
</script>

<template>
  <div class="header">
    <a href="#">首页</a>
    <a href="#">水果种类</a>
    <a href="#">关于我们</a>
    <a href="#">联系我们</a>
    <a href="#"><i class="bi bi-box-arrow-in-right"></i>登录</a>
  </div>

  <div class="main">
    <h2>水果目录</h2>
    <div class="tab">
      <button class="tablinks">苹果</button>
      <button class="tablinks">香蕉</button>
      <button class="tablinks">西瓜</button>
    </div>

    <div class="fruit-list">
      <ul>
        <li> 1</li>
        <li> 1</li>
        <li> 1</li>
        <li> 1</li>
        <li> 1</li>
        <li> 1</li>
        <li> 1</li>
        <li> 1</li>
        <li> 1</li>
      </ul>
    </div>
  </div>

</template>

<style scoped lang="scss">
* {
  box-sizing: border-box;
  font-family: Arial, Helvetica, sans-serif;
}

.header {
  background-color: #0099FF;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 0 1px;

  a {
    font-size: 18px;
    padding: 15px;
    text-decoration: none;

    .bi {
      margin-right: 5px;
    }

    &:hover,
    &:active {
      background-color: #00CCFF;
      color: #F5F9FF;
    }
  }

  @media screen and (max-width: 600px) {
    font-size: 18px;
    flex-direction: column;
    align-items: flex-start;
    padding: 10px;
    width: 100vw;
    /* 占满整个视口宽度 */
    min-width: 320px;
    /* 确保在极小屏幕上不被过度压缩 */
  }
}

.main {
  h2 {
    color: #4d7c0f;
  }

  .tab {
    float: left;
    border: 1px solid #e0f2e9;
    background-color: #f0fdf4;
    width: 30%;
    height: auto;

    button {
      display: block;
      background-color: #fff;
      color: #f97316;
      padding: 22px 16px;
      width: 100%;
      border: none;
      outline: none;
      text-align: center;
      cursor: pointer;
      transition: 0.3s;
      font-size: 17px;
      margin: 10px 0;
      border-radius: 6px;

      &:hover {
        background-color: #fff7ed;
        color: #ea580c;
      }

      &:active {
        background-color: #f97316;
        color: #fff;
      }
    }
  }

  .fruit-list {
    float: right;

  }
}
</style>
