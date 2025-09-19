// src/api/notice.js
import apiClient from "./axios";

export function fetchNotices(params) {
  return apiClient.get("notice/notices/", { params });
}

export function createNotice(data) {
  return apiClient.post("notice/notices/", data);
}

export function updateNotice(id, data) {
  return apiClient.put(`notice/notices/${id}/`, data);
}

export function fetchCategories() {
  return apiClient.get("notice/categories/");
}

export function createCategory(data) {
  return apiClient.post("notice/categories/", data);
}