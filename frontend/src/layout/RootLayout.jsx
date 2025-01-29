import React, { useEffect } from "react";
import { Outlet, useNavigate } from "react-router";
import useUserStore from "../store/userStore";

const RootLayout = () => {
  const navigate = useNavigate();
  const { user } = useUserStore();

  useEffect(() => {
    if (user && Object.keys(user).length > 0) {
      navigate("/user/dashboard"); // Navigate to dashboard if user exists
    } else {
      navigate("/register"); // Navigate to register if user does not exist
    }
  }, [user, navigate]);

  return (
    <div className="h-screen w-screen flex flex-col">
      {/* Navbar */}
      {/* <div className="h-[50px] bg-gray-800 text-white flex items-center px-4">
        Navbar
      </div> */}

      {/* Content Area */}
      <div className="flex-1 overflow-auto">
        <Outlet />
      </div>
    </div>
  );
};

export default RootLayout;
