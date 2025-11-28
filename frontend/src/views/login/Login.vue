<script setup>
  import { ref, reactive } from 'vue'
  import Loading from '@/components/Loading.vue'
  import LoginForm from './LoginForm.vue' // 导入登录子组件
  import RegisterForm from './RegisterForm.vue' // 导入注册子组件
  import { isLogin, changeForm, showPassword, togglePassword } from '@/utils/useAuthForm'
  import { userRegisterApi } from '@/api/register'

  const isLoading = ref(false) // 控制loading显示/隐藏
  // 新增：定义响应式的表单数据对象，存储登录/注册的输入内容
  const form = reactive({
    username: '', // 用户名
    email: '', // 注册邮箱
    password: '', // 密码
  })
  // 获取子组件的引用
  const registerFormRef = ref(null)

  // 定义验证规则函数
  const validateUsername = (username) => {
    const trimmed = username?.trim()
    if (!trimmed) {
      // 返回错误信息对象，方便区分错误类型或用于国际化
      return { isValid: false, message: '请输入用户名！' }
    }
    if (trimmed.length < 3 || trimmed.length > 10) {
      return { isValid: false, message: '用户名长度需在3-10个字符之间！' }
    }
    const usernameReg = /^[\u4e00-\u9fa5a-zA-Z0-9_]{3,10}$/
    if (!usernameReg.test(trimmed)) {
      return { isValid: false, message: '用户名仅允许包含字母、数字、下划线和中文！' }
    }
    return { isValid: true } // 成功时不带消息或带空消息
  }

  const validateEmail = (email) => {
    const trimmed = email?.trim()
    if (!trimmed) {
      return { isValid: false, message: '请输入注册邮箱！' }
    }
    if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(trimmed)) {
      return { isValid: false, message: '请输入合法的邮箱格式！' }
    }
    return { isValid: true }
  }

  const validatePassword = (password) => {
    if (!password) {
      // 密码通常不应 trim
      return { isValid: false, message: '请输入密码！' }
    }
    if (password.length < 6) {
      return { isValid: false, message: '密码长度至少6位！' }
    }
    // 可以在这里添加更多密码强度检查...
    return { isValid: true }
  }

  // 修改后的 handleRegister 函数
  const handleRegister = async (e) => {
    e.preventDefault()
    isLoading.value = true

    // 执行验证
    const usernameValidation = validateUsername(form.username)
    if (!usernameValidation.isValid) {
      alert(usernameValidation.message)
      isLoading.value = false
      return // 阻止继续执行
    }

    const emailValidation = validateEmail(form.email)
    if (!emailValidation.isValid) {
      alert(emailValidation.message)
      isLoading.value = false
      return
    }

    const passwordValidation = validatePassword(form.password)
    if (!passwordValidation.isValid) {
      alert(passwordValidation.message)
      isLoading.value = false
      return
    }

    // 如果所有验证都通过，则继续执行注册逻辑
    try {
      isLoading.value = true
      // API调用
      const res = await userRegisterApi(form)

      alert('注册成功')
      console.log('注册成功', res, registerFormRef.value)
      // 成功后重置表单
      registerFormRef.value.resetForm()
      // 可以在这里添加成功提示或路由跳转
    } catch (error) {
      alert('注册失败:' + error.message)
      console.error('注册失败:', error)

      // 可以根据 error 内容显示更具体的错误信息
    } finally {
      isLoading.value = false
    }
  }

  // 模拟登录请求（实际项目替换为接口请求）
  const handleLogin = async (e) => {
    e.preventDefault() // 阻止表单默认提交
    isLoading.value = true // 显示loading
    try {
      // 模拟接口请求（延迟2秒）
      await new Promise((resolve) => setTimeout(resolve, 2000))
      // 请求成功后逻辑...
      console.log(isLogin.value ? '登录成功' : '注册成功')
    } catch (error) {
      console.error(isLogin.value ? '登录失败:' : '注册失败:', error)
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

    <!-- 动态渲染登录/注册子组件，传递核心方法和状态 -->
    <LoginForm
      v-if="isLogin"
      :show-password="showPassword"
      @toggle-password="togglePassword"
      @change-form="changeForm"
      @submit="handleLogin"
      :is-loading="isLoading"
    />
    <RegisterForm
      v-else
      ref="registerFormRef"
      :show-password="showPassword"
      @toggle-password="togglePassword"
      @change-form="changeForm"
      @submit="handleRegister"
      :is-loading="isLoading"
      :form="form"
    />
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
  }

  @media screen and (max-width: 768px) {
    .bg {
      height: calc(100vh - 60px);
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
    }
  }
</style>
