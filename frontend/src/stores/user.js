// src/stores/user.js
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserStore = defineStore('user', () => {
  // 状态：是否登录、用户名
  const isLoggedIn = ref(false)
  const username = ref('')

  // 登录方法：存入用户名并持久化到本地
  const login = (userName) => {
    isLoggedIn.value = true
    username.value = userName
    localStorage.setItem('user', JSON.stringify({ isLoggedIn: true, username: userName }))
  }

  // 退出方法：清除状态和本地存储
  const logout = () => {
    isLoggedIn.value = false
    username.value = ''
    localStorage.removeItem('user')
  }

  // 初始化：页面刷新后从本地恢复状态
  const initUser = () => {
    const userStr = localStorage.getItem('user')
    if (userStr) {
      const user = JSON.parse(userStr)
      isLoggedIn.value = user.isLoggedIn
      username.value = user.username
    }
  }

  return { isLoggedIn, username, login, logout, initUser }
})