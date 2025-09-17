import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: null,
    departments: [],
    roles: [],
  }),
  actions: {
    setUser(userData) {
      this.user = userData;
      this.departments = userData.departments || [];
      this.roles = userData.roles || [];
    },
    clearUser() {
      this.user = null;
      this.departments = [];
      this.roles = [];
    },
  },
});