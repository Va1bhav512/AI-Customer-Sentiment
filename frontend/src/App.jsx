import { createBrowserRouter, RouterProvider, useNavigate } from "react-router";

// Pages
import RootLayout from "./layout/RootLayout";
import Register from "./pages/Auth/Register";
import DashBoard from "./pages/User/DashBoard";
import UserLayout from "./layout/UserLayout";
import Analytics from "./pages/User/Analytics";
import FocusArea from "./pages/User/FocusArea";
import Recommendations from "./pages/User/Recommendation";
import AIToBeAddedPage from "./pages/User/AIToBeAddedPage.jsx";
import SettingsPage from "./pages/User/Settings.jsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <RootLayout />,
    children: [
      {
        path: "register",
        element: <Register />,
      },
    ],
  },
  {
    path: "/user",
    element: <UserLayout />,
    children: [
      {
        path: "dashboard",
        element: <DashBoard />,
      },
      {
        path: "focus-area",
        element: <FocusArea />,
      },
      {
        path: "recommendations",
        element: <Recommendations />,
      },
      {
        path: "ai-assistant",
        element: <AIToBeAddedPage />,
      },
      {
        path: "settings",
        element: <SettingsPage />,
      },
      {
        path: "analytics",
        element: <Analytics />,
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router}></RouterProvider>;
}

export default App;
