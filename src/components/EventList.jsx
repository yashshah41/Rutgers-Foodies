import React, { useState } from "react";
import data from "../assets/data.json";

const EventBox = ({ event }) => {
  const [expanded, setExpanded] = useState(false);

  const toggleDescription = () => {
    setExpanded(!expanded);
  };

  // Adjust the height dynamically based on the 'expanded' state.
  const heightClass = expanded ? "h-auto" : "h-48"; 

  return (
    <div className={`border-2 border-red-200 rounded-lg shadow hover:shadow-lg transition-shadow duration-300 ease-in-out overflow-hidden ${heightClass}`}>
      <div className="p-6">
        <h2 className="text-xl font-bold text-red-600 mb-2">{event.name}</h2>
        <p className="text-gray-600 text-sm">
          {event.startsOn} - {event.endsOn}
          <br />
          Hosted by: {event.organizationName}
        </p>
        <div className={`text-gray-800 mt-2 ${expanded ? "block" : "hidden"}`}>
          {event.description}
        </div>
        {!expanded && (
          <button
            className="text-red-500 mt-2 cursor-pointer hover:underline focus:outline-none transition duration-200 ease-in-out"
            onClick={toggleDescription}
          >
            Read More
          </button>
        )}
      </div>
    </div>
  );
};

const EventList = () => {
  return (
    <div className="container mx-auto p-6">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {data.map((event, index) => (
          <EventBox key={index} event={event} />
        ))}
      </div>
    </div>
  );
};

export default EventList;
