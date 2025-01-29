import React from "react";
import { FaRobot } from "react-icons/fa";

const AIToBeAddedPage = () => {
  return (
    <div className="bg-[#f4f7fc] h-full p-8 flex flex-col items-center justify-center">
      <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg">
        <div className="flex justify-center mb-4">
          <FaRobot className="text-6xl text-gray-600" />
        </div>
        <h1 className="text-3xl font-bold text-center mb-4">AI Assistant Coming Soon</h1>
        <p className="text-lg text-center text-gray-600 mb-6">
          The AI Assistant feature is currently being developed and will be available soon.
        </p>
        <p className="text-md text-center text-gray-500">
          Stay tuned for updates and check back for when this feature is added to help you manage tasks,
          provide insights, and assist with decision-making.
        </p>

        <div className="mt-8 text-center">
          <button className="bg-blue-500 text-white py-2 px-6 rounded-full text-xl font-semibold cursor-pointer">
            Notify Me When Live
          </button>
        </div>
      </div>
    </div>
  );
};

export default AIToBeAddedPage;
