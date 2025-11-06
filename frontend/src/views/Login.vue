<script setup>
  import Footer from '@/components/Footer.vue'
  import Header from '@/components/Header.vue'
  import { ref } from 'vue'

  // 控制密码框显示
  const showPassword = ref(false) // 定义变量，控制密码是否可见-默认不可见

  // 切换密码可见性的方法
  const togglePassword = () => {
    showPassword.value = !showPassword.value
  }
</script>
<template>
  <Header></Header>
  <div class="bg"></div>
  <div class="login">
    <div class="login-banner">
      <div class="banner-content">
        <h3>欢迎回来</h3>
        <p>请登录您的账户以继续使用我们的服务，体验更多专属功能。</p>

        <div class="feature-item">
          <i class="bi bi-shield-fill"></i>
          <div>
            <h4>安全保障</h4>
            <p>多重加密保护您的账户安全</p>
          </div>
        </div>

        <div class="feature-item">
          <i class="bi bi-lightning-charge-fill"></i>
          <div>
            <h4>快速访问</h4>
            <p>一键登录，无缝体验</p>
          </div>
        </div>
      </div>

      <div class="banner-footer">© 2025 您的品牌名称 保留所有权利</div>
    </div>

    <form
      class="login-form"
      action="#"
      method="get"
    >
      <h3>账户登录</h3>
      <p>请输入您的账户信息</p>
      <!-- 用户名输入 -->
      <div class="login-name">
        <input
          type="text"
          name="username"
          placeholder="用户名/邮箱"
          required
        />
      </div>

      <!-- 密码输入 -->
      <div class="login-password">
        <input
          class="pwd"
          :type="showPassword ? 'text' : 'password'"
          name="pwd"
          placeholder="密码"
          required
        />
        <i
          class="bi bi-eye"
          @click="togglePassword"
          v-show="!showPassword"
        ></i>
        <i
          class="bi bi-eye-slash"
          @click="togglePassword"
          v-show="showPassword"
        ></i>
      </div>

      <div class="login-button">
        <div class="re-pwd">
          <a
            class="register"
            href="#"
          >
            立即注册
          </a>
          <a href="#">忘记密码？</a>
        </div>
        <button
          type="submit"
          name="login"
        >
          登录
        </button>
      </div>
    </form>
  </div>

  <Footer></Footer>
</template>

<style scoped lang="scss">
  .bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    background: url(../../public/images/preview.jpg) no-repeat center;
    background-size: cover;
  }

  .login {
    display: flex; // 左右分栏
    min-height: calc(100vh - 276px);
    overflow: hidden; // 避免内容溢出
    margin: 50px auto;
    max-width: 1200px;

    .login-banner {
      flex: 1; // 占比 50% 左右
      background: linear-gradient(160deg, #1b64ff, #31acfb); // 渐变蓝色背景
      color: #fff;
      padding: 40px;
      display: flex;
      flex-direction: column;
      justify-content: space-around;

      .banner-content {
        h3 {
          font-size: 30px;
          margin-bottom: 20px;
        }

        p {
          font-size: 14px;
          line-height: 1.6;
        }

        .feature-item {
          display: flex;
          align-items: flex-start;
          margin-top: 30px;
          margin-bottom: 25px;
          padding: 5px 5px 5px 0;

          i {
            font-size: 24px;
            margin-right: 12px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            padding: 10px;
          }

          h4 {
            font-size: 16px;
            margin-top: 4px;
          }

          p {
            font-size: 13px;
            margin: 0;
            opacity: 0.9;
          }
        }
      }

      .banner-footer {
        font-size: 12px;
        opacity: 0.8;
      }
    }

    .login-form {
      flex: 1; // 与左侧占比一致
      padding: 40px;
      background: #f9fafb;
      display: flex;
      flex-direction: column;
      justify-content: center;

      .login-name {
        & [type='text'] {
          border-radius: 10px;
          border: 1px solid #f1f2f5;
          box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
          margin-bottom: 20px;
          padding: 10px;
          width: 100%;
        }
      }

      .login-password {
        position: relative;

        .pwd {
          border-radius: 10px;
          border: 1px solid #f1f2f5;
          box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
          margin-bottom: 20px;
          padding: 10px;
          width: 100%;
          padding-right: 35px;

          // 隐藏 Chrome/Safari 等 WebKit 内核浏览器的默认眼睛图标
          &::-webkit-credentials-cramble-button,
          &::-webkit-reveal {
            display: none;
          }

          // 隐藏 Edge/IE 浏览器的默认眼睛图标
          &::-ms-reveal {
            display: none;
          }
        }

        .bi {
          position: absolute;
          right: 4%;
          top: 38%;
          transform: translateY(-50%);
          cursor: pointer;
        }
      }

      .login-button {
        & [type='submit'] {
          background-color: #24f563;
          border: none;
          border-radius: 10px;
          color: white;
          padding: 12px 25px;
          text-align: center;
          font-size: 18px;
          width: 100%;
        }

        .re-pwd,
        a {
          text-decoration: none;
          color: #2b99fc;

          .register {
            float: right;
            margin-bottom: 20px;
          }
        }
      }
    }
  }

  @media screen and (max-width: 600px) {
    .bg {
      height: calc(100vh - 61px);
    }

    .login {
      max-width: 100%; // 占满屏幕宽度
      display: flex;
      justify-content: center;
      align-items: center;

      .login-banner {
        display: none;
      }

      .login-form {
        max-width: 400px;
        margin: 0;
        padding: 30px 20px;
      }
    }
  }
</style>
