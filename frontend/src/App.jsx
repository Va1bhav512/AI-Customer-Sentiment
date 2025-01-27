import { createBrowserRouter, RouterProvider } from "react-router";

// Pages
import RootLayout from "./layout/RootLayout";

const router = createBrowserRouter([
  {
    path: "/",
    element: <RootLayout />,
  },
]);

function App() {
  return <RouterProvider router={router}></RouterProvider>;
}

export default App;
