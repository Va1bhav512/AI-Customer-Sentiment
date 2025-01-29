import React, { useState } from "react";
import { FaUser, FaBell, FaLock, FaSave } from "react-icons/fa";

const SettingsPage = () => {
  const [isEmailNotificationsEnabled, setIsEmailNotificationsEnabled] = useState(true);
  const [isSmsNotificationsEnabled, setIsSmsNotificationsEnabled] = useState(false);

  return (
    <div className="bg-[#F7FAFC] h-full p-8 rounded-xl shadow-xl">
      <div className="bg-white p-8 rounded-xl shadow-md">
        <h1 className="text-4xl font-extrabold text-center text-gray-800 mb-10">
          Settings
        </h1>

        {/* Profile Settings */}
        <div className="mb-10">
          <h2 className="text-2xl font-semibold text-gray-800 mb-6">Profile Settings</h2>
          <div className="flex items-center gap-6 mb-6">
            <FaUser className="text-gray-600 text-3xl" />
            <div className="flex flex-col w-full">
              <label htmlFor="username" className="text-gray-600 text-lg">Username</label>
              <input
                id="username"
                type="text"
                placeholder="Enter your username"
                className="p-3 border border-gray-300 rounded-md mt-2 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
              />
            </div>
          </div>
        </div>

        {/* Notification Settings */}
        <div className="mb-10">
          <h2 className="text-2xl font-semibold text-gray-800 mb-6">Notification Settings</h2>
          
          {/* Email Notifications */}
          <div className="flex items-center gap-6 mb-6">
            <FaBell className="text-gray-600 text-3xl" />
            <div className="flex flex-col w-full">
              <label htmlFor="email-notifications" className="text-gray-600 text-lg">Email Notifications</label>
              <div className="flex justify-between items-center">
                <p className="text-gray-500">Receive email notifications</p>
                <input
                  id="email-notifications"
                  type="checkbox"
                  checked={isEmailNotificationsEnabled}
                  onChange={() => setIsEmailNotificationsEnabled(!isEmailNotificationsEnabled)}
                  className="toggle-checkbox"
                />
              </div>
            </div>
          </div>

          {/* SMS Notifications */}
          <div className="flex items-center gap-6 mb-6">
            <FaBell className="text-gray-600 text-3xl" />
            <div className="flex flex-col w-full">
              <label htmlFor="sms-notifications" className="text-gray-600 text-lg">SMS Notifications</label>
              <div className="flex justify-between items-center">
                <p className="text-gray-500">Receive SMS notifications</p>
                <input
                  id="sms-notifications"
                  type="checkbox"
                  checked={isSmsNotificationsEnabled}
                  onChange={() => setIsSmsNotificationsEnabled(!isSmsNotificationsEnabled)}
                  className="toggle-checkbox"
                />
              </div>
            </div>
          </div>
        </div>

        {/* Security Settings */}
        <div className="mb-10">
          <h2 className="text-2xl font-semibold text-gray-800 mb-6">Security Settings</h2>
          <div className="flex items-center gap-6 mb-6">
            <FaLock className="text-gray-600 text-3xl" />
            <div className="flex flex-col w-full">
              <label htmlFor="password" className="text-gray-600 text-lg">Password</label>
              <input
                id="password"
                type="password"
                placeholder="Change your password"
                className="p-3 border border-gray-300 rounded-md mt-2 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
              />
            </div>
          </div>
        </div>

        {/* Save Settings */}
        <div className="flex justify-center mt-10">
          <button
            className="bg-blue-600 text-white py-3 px-8 rounded-full flex items-center gap-3 text-lg font-semibold hover:bg-blue-700 transition-all"
          >
            <FaSave />
            Save Settings
          </button>
        </div>
      </div>
    </div>
  );
};

export default SettingsPage;
