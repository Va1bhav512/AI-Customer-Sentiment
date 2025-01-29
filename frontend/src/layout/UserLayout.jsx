import React, { useEffect } from "react";
import SideBar from "../pages/Navbars/SideBar";
import { Outlet, useLocation, useNavigate } from "react-router";
import useUserStore from "../store/userStore";

const UserLayout = () => {
  const navigate = useNavigate();
  const { user } = useUserStore();
  const location = useLocation();

  useEffect(() => {
    if (user && Object.keys(user).length > 0) {
      if (location.pathname === "/user") {
        navigate("/user/dashboard");
      }
    } else {
      navigate("/register"); // Navigate to register if user does not exist
    }
  }, [user, navigate]);

  return (
    <div className="h-screen flex flex-col">
      <div>
        <SideBar />
      </div>

      <div className="ml-[225px] flex-1">
        <Outlet />
      </div>
    </div>
  );
};

export default UserLayout;
