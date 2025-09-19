// src/api/menu.js
import apiClient from "./axios";

export function fetchMenus() {
  return apiClient.get("core/menus/");
}