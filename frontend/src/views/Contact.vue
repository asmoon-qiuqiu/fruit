<script setup>
  import TxMap from '@/components/TxMap.vue'
</script>

<template>
  <div class="contact">
    <div class="contact-mask">
      <div class="contact-content">
        <h4>联系方式</h4>
        <h6>网站问题&建议意见</h6>
        <p>Email：2371824615@qq.com</p>
        <p>QQ：2371824615</p>
        <hr />
      </div>
      <div class="contact-content">
        <h6>微信</h6>
        <img
          src="@public/images/wx.jpg"
          alt="微信"
        />
        <hr />
      </div>
      <div class="contact-content">
        <h6>地址</h6>
        <TxMap></TxMap>
        <hr />
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
  $primary-color: #fff0f5; // 主题颜色变量
  $minor-color: #c2185b;
  .contact {
    min-height: calc(100vh - 176px);
    background: url('@public/images/contact.jpg') no-repeat center;
    background-size: cover;
    background-attachment: fixed;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-flow: column wrap; // 子元素垂直排列并在需要时换行

    .contact-mask {
      background: rgba(253, 231, 233, 0.8);
      width: 50%;
      padding: 10px;
      margin: 20px 0;
      overflow: auto;
      .contact-content {
        color: $minor-color;
        padding: 10px;
        h4 {
          margin-bottom: 15px;
        }
        hr {
          width: 100%;
        }
        p {
          text-indent: 1em;
          line-height: 16px;
        }
        img {
          width: 200px;
          height: 200px;
          display: block;
          margin-top: 10px;
        }
      }
    }
  }
</style>
