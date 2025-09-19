// frontend/src/api/auth.js
import apiClient from "./axios";

export function login(username, password) {
  return apiClient.post("accounts/auth/login/", { username, password });
}

export function logout() {
  return apiClient.post("accounts/auth/logout/");
}

export function authStatus() {
  return apiClient.get("accounts/auth/status/");
}