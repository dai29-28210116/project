import { defineStore } from "pinia";

export const useUiStore = defineStore("ui", {
  state: () => ({
    snackbar: {
      show: false,
      text: "",
      color: "success",
    },
  }),
  actions: {
    showSnackbar(text, color = "success") {
      this.snackbar.text = text;
      this.snackbar.color = color;
      this.snackbar.show = true;
    },
    hideSnackbar() {
      this.snackbar.show = false;
      this.snackbar.text = "";
    },
  },
});
