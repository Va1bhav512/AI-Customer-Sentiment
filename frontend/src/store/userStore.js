import axios from "axios";
import { create } from "zustand";
import { persist } from "zustand/middleware";

const useUserStore = create(
  persist(
    (set, get) => ({
      user: {},
      overAllAnalysis: {},
      setUser: (user) => set({ user }),
      logOutUser: () => {
        localStorage.removeItem("user-session");
        set({ user: {} });
      },
      setOverallAnalysisMain: (analysis) => set({ overAllAnalysis: analysis }),
      clearOverallAnalysisMain: () => set({ overAllAnalysis: {} }),
      fetchReview: async () => {
        const { user } = get(); // Access the current user state

        if (!user?.email) {
          console.error("User email is not available. Please log in.");
          return;
        }

        try {
          const response = await axios.get(
            `http://127.0.0.1:8000/user/${user.email}`
          );
          console.log("Fetched Reviews: ", response.data);
          // Update the user with the fetched reviews if necessary
          set((state) => ({
            user: { ...state.user, reviews: response.data.reviews },
          }));
        } catch (error) {
          console.error("Error fetching user reviews:", error);
        }
      },
    }),
    {
      name: "user-session", // the key used in localStorage to store the session
      getStorage: () => localStorage, // use localStorage to persist the state
    }
  )
);

export default useUserStore;
