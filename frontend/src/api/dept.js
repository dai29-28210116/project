import apiClient from "./axios";

export function fetchDepartments() {
  return apiClient.get("accounts/departments/");
}