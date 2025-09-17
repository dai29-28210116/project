// src/api/axios.js
import axios from "axios";

// Cookie から csrftoken を取り出す関数
function getCsrfToken() {
  const match = document.cookie.match(/csrftoken=([\w-]+)/);
  return match ? match[1] : "";
}

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,  // 例: http://127.0.0.1:8000/api/
  withCredentials: true,                       // Cookie を必ず送る
});

// リクエスト時に CSRF ヘッダを自動追加
apiClient.interceptors.request.use((config) => {
  const token = getCsrfToken();
  if (token) {
    config.headers["X-CSRFToken"] = token;
  }
  return config;
});

export default apiClient;
