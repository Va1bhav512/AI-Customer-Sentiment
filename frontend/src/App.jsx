import { createBrowserRouter, RouterProvider } from "react-router";

// Pages
import RootLayout from "./layout/RootLayout";
import Register from "./pages/Auth/Register";
import DashBoard from "./pages/User/DashBoard";

const router = createBrowserRouter([
  {
    path: "/",
    element: <RootLayout />,
    children: [
      {
        path: "register",
        element: <Register />
      },
      {
        path: "dashboard",
        element: <DashBoard />
      }
    ],
  },
]);

function App() {
  return <RouterProvider router={router}></RouterProvider>;
}

export default App;
