import apiClient from "./axios";

export function login(username, password) {
  return apiClient.post("auth/login/", { username, password });
}

export function logout() {
  return apiClient.post("auth/logout/");
}

export function authStatus() {
  return apiClient.get("auth/status/");
}