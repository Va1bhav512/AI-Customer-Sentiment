import { create } from "zustand";
import { persist } from "zustand/middleware";

const useUserStore = create(
  persist(
    (set) => ({
      user: {},
      setUser: (user) => set({ user }),
      logOutUser: () => {
        localStorage.removeItem("user-session");
        set({ user: {} });
      },
    }),
    {
      name: "user-session", // the key used in localStorage to store the session
      getStorage: () => localStorage, // use localStorage to persist the state
    }
  )
);

export default useUserStore;
