// src/utils/request.js
import axios from "axios"

// 1. 创建Axios实例，配置基础参数
const service = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL, // 后端接口的基础域名，后续请求只需写相对路径
    timeout: 5000, // 请求超时时间（5秒）
    headers: {
        "Content-Type": "application/json;charset=utf-8", // 默认请求头
    },
});

// 2. 请求拦截器：发送请求前的处理（如添加token、请求参数格式化）
service.interceptors.request.use(
    (config) => {
        // 示例：若有登录token，可在此处添加到请求头
        // const token = localStorage.getItem("token");
        // if (token) {
        //   config.headers.Authorization = `Bearer ${token}`;
        // }
        return config;
    },
    (error) => {
        // 请求错误的统一处理
        console.error("请求拦截器错误：", error);
        return Promise.reject(error);
    }
);

// 3. 响应拦截器：接收响应后的处理（统一错误码、数据格式化）
service.interceptors.response.use(
    (response) => {
        // 只返回响应的data部分，简化前端获取数据的逻辑
        return response.data;
    },
    (error) => {
        // 统一处理响应错误
        console.error("响应错误：", error);
        let errorMsg = "请求失败，请稍后重试";

        // 根据错误类型提取具体提示信息
        if (error.response) {
            // 服务端返回的错误（有状态码）
            const { status, data } = error.response;
            switch (status) {
                case 400:
                    // 业务逻辑错误（如用户名已存在）
                    errorMsg = data.detail || "参数错误";
                    break;
                case 422:
                    // 数据校验错误（如用户名格式不对）
                    errorMsg = data.detail?.[0]?.msg || "数据格式错误";
                    break;
                case 500:
                    errorMsg = "服务器内部错误";
                    break;
                case 401:
                    errorMsg = "未登录，请先登录";
                    // 示例：未登录时跳转到登录页
                    // window.location.href = "/login";
                    break;
                default:
                    errorMsg = data.message || errorMsg;
            }
        } else if (error.request) {
            // 网络请求已发送，但无响应（如后端服务未启动）
            errorMsg = "网络异常，请检查后端服务是否运行";
        }

        // 可以在此处统一弹出错误提示（如使用Element Plus的Message）
        // ElMessage.error(errorMsg);

        // 返回错误信息，让业务页面自行处理
        return Promise.reject({ message: errorMsg });
    }
);

// 4. 暴露封装后的Axios实例
export default service;