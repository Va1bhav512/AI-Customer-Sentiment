import React from "react";
import { FaHome } from "react-icons/fa";
import { TfiTarget } from "react-icons/tfi";
import { FaNewspaper } from "react-icons/fa6";
import { MdOutlineRecommend } from "react-icons/md";
import { FaGear } from "react-icons/fa6";
import { TbDeviceAnalytics } from "react-icons/tb";
import { MdLogout } from "react-icons/md";
import USER from "/user.png";

import { Link, useNavigate, useLocation } from "react-router";
import useUserStore from "../../store/userStore";

const SideBar = () => {
  const { user, logOutUser } = useUserStore();
  const navigate = useNavigate();
  const location = useLocation();

  const iconsArray = [
    FaHome,
    TfiTarget,
    FaNewspaper,
    MdOutlineRecommend,
    FaGear,
    TbDeviceAnalytics,
  ];

  const listNames = [
    "Home",
    "Focus Area",
    "Recommendations",
    "AI Assistant",
    "Settings",
    "Analytics",
  ];

  const listRoutes = [
    "/user/dashboard",
    "/user/focus-area",
    "/user/recommendations",
    "/user/ai-assistant",
    "/user/settings",
    "/user/analytics",
  ];

  const handleLogout = () => {
    logOutUser();
    navigate("/register");
  };

  return (
    <div className="bg-[#F2F6FA] h-screen fixed flex flex-col justify-between w-[225px] py-4 px-4">
      {/* User Section */}
      <div className="flex items-center gap-2">
        <div className="bg-[#D9D9D9] rounded-full items-center justify-center">
          <img src={USER} alt="" className="h-8 w-8" />
        </div>

        {user ? (
          <h1 className="font-bold text-2xl">{user.cname}</h1>
        ) : (
          <h1>Please Login!</h1>
        )}
      </div>

      {/* Navigation Links */}
      <ul className="h-2/3 flex flex-col justify-center gap-4">
        {iconsArray.map((Icon, index) => {

          const isActive = location.pathname === listRoutes[index]; // Check if the current route matches
          return (
            <Link to={listRoutes[index]} key={index}>
              <div
                className={`flex items-center gap-2 rounded-lg p-2 cursor-pointer ${
                  isActive
                    ? "bg-[#0660FE] text-white"
                    : "hover:bg-[#0660FE] hover:text-white"
                }`}
              >
                <Icon className={`${isActive ? "text-white" : ""}`} />
                <p>{listNames[index]}</p>
              </div>
            </Link>
          );
        })}
      </ul>

      {/* Logout */}
      <div
        onClick={handleLogout}
        className="flex items-center gap-2 hover:bg-[#0660FE] rounded-lg p-2 hover:text-white cursor-pointer"
      >
        <MdLogout />
        <p>Logout</p>
      </div>
    </div>
  );
};

export default SideBar;
