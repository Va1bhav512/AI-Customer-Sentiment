import { create } from "zustand";

const userStore = create((set) => ({
  user: {},
  setUser: (user) => set({ user }),
}));
