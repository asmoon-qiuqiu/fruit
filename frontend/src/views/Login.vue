<script setup>
  import { ref } from 'vue'
  import Loading from '@/components/Loading.vue'
  const isLogin = ref(true) // 控制登录注册切换
  const isLoading = ref(false) // 控制loading显示/隐藏

  // 切换登录注册的方法
  const changeForm = () => {
    isLogin.value = !isLogin.value
  }

  // 控制密码框显示
  const showPassword = ref(false) // 定义变量，控制密码是否可见-默认不可见

  // 切换密码可见性的方法
  const togglePassword = () => {
    showPassword.value = !showPassword.value
  }

  // 新增：模拟登录/注册请求（实际项目替换为接口请求）
  const handleSubmit = async (e) => {
    e.preventDefault() // 阻止表单默认提交
    isLoading.value = true // 显示loading
    try {
      // 模拟接口请求（延迟2秒）
      await new Promise((resolve) => setTimeout(resolve, 2000))
      // 请求成功后逻辑...
      console.log('操作完成')
    } catch (error) {
      console.error('操作失败:', error)
      // 处理错误
    } finally {
      // 无论成功与否都关闭 loading
      isLoading.value = false
    }
  }
</script>
<template>
  <!-- 引入Loading组件，通过isLoading控制显示 -->
  <Loading
    :visible="isLoading"
    :text="isLogin ? '登录中...' : '注册中...'"
  />
  <div class="bg"></div>
  <div class="login">
    <div class="login-banner">
      <div class="banner-content">
        <h3>欢迎回来</h3>
        <p>请登录您的账户，继续探索新鲜水果世界。</p>

        <div class="feature-item">
          <i class="bi bi-apple"></i>
          <div>
            <h4>品质保障</h4>
            <p>严选果园直供，多重质检确保新鲜安全</p>
          </div>
        </div>

        <div class="feature-item">
          <i class="bi bi-lightning-charge-fill"></i>
          <div>
            <h4>极速体验</h4>
            <p>一键登录，新鲜水果随时随地选购</p>
          </div>
        </div>
      </div>

      <div class="banner-footer">© 2025 asmoon 保留所有权利</div>
    </div>
    <!-- 登录表单 -->
    <form
      class="login-form"
      action="#"
      method="get"
      v-if="isLogin"
      @submit="handleSubmit"
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
          v-show="showPassword"
        ></i>
        <i
          class="bi bi-eye-slash"
          @click="togglePassword"
          v-show="!showPassword"
        ></i>
      </div>

      <div class="login-button">
        <div class="re-pwd">
          <a
            class="register"
            @click="changeForm"
          >
            立即注册
          </a>
          <a href="#">忘记密码？</a>
        </div>
        <button
          type="submit"
          name="login"
          :disabled="isLoading"
        >
          {{ isLoading ? '加载中...' : '登录' }}
        </button>
      </div>
    </form>

    <!-- 注册表单 -->
    <form
      class="login-form"
      action="#"
      method="get"
      @submit="handleSubmit"
      v-else
    >
      <h3>账户注册</h3>
      <p>请输入您的账户信息</p>
      <!-- 用户名输入 -->
      <div class="login-name">
        <input
          type="text"
          name="username"
          placeholder="用户名"
          required
        />
      </div>
      <!-- 邮箱输入 -->
      <div class="login-name">
        <input
          type="email"
          name="email"
          placeholder="邮箱"
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
          v-show="showPassword"
        ></i>
        <i
          class="bi bi-eye-slash"
          @click="togglePassword"
          v-show="!showPassword"
        ></i>
      </div>

      <div class="login-button">
        <div class="re-pwd">
          <a
            class="register"
            @click="changeForm"
          >
            已有账号？登录
          </a>
          <a href="#">忘记密码？</a>
        </div>
        <button
          type="submit"
          name="login"
          :disabled="isLoading"
        >
          {{ isLoading ? '加载中...' : '注册' }}
        </button>
      </div>
    </form>
  </div>
</template>

<style scoped lang="scss">
  .bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    background: url('@public/images/login.jpg') no-repeat center;
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
      background: linear-gradient(120deg, #fff0f5, #c2185b); // 渐变背景
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
        & [type='text'],
        [type='email'] {
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
          background-color: #db729b;
          border: none;
          border-radius: 10px;
          color: white;
          padding: 12px 25px;
          text-align: center;
          font-size: 18px;
          width: 100%;
          &:hover {
            background-color: #c2185b;
            cursor: pointer;
          }
        }

        .re-pwd,
        a {
          text-decoration: none;
          color: #2b99fc;

          .register {
            float: right;
            margin-bottom: 20px;
            cursor: pointer;
          }
        }
      }
    }
  }

  @media screen and (max-width: 768px) {
    .bg {
      height: calc(100vh - 61px);
    }

    .login {
      max-width: 90%; // 占满屏幕宽度
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 65px 0;
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
