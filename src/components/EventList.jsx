import React, { useState } from "react";
import data from "../assets/data.json";

const EventBox = ({ event }) => {
  const [expanded, setExpanded] = useState(false);

  const toggleDescription = () => {
    setExpanded(!expanded);
  };

  return (
    <div className="border-2 border-black">
      <div className={`bg-white rounded-lg w-72 p-6 m-4 flex flex-col transform hover:scale-105 transition-transform duration-300 ease-in-out shadow-m ${
          expanded ? "h-auto" : "h-72"
        } overflow-hidden`}
      >
        <h2 className="text-2xl font-bold mb-2 text-red-600">{event.name}</h2>
        <p className="text-gray-500">
          {event.startsOn} - {event.endsOn}
          <br>
          </br>
          Hosted by: {event.organizationName}

        </p>
        <div className={`text-gray-800 mt-2 ${expanded ? "" : "truncate"}`}>
          {expanded ? event.description : event.description.substring(0, 100)}
        </div>
        {!expanded && event.description.length > 100 && (
          <button
            className="text-blue-500 mt-2 cursor-pointer hover:underline"
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
    <div className="flex flex-wrap gap-6 justify-center">
      {data.map((event, index) => (
        <EventBox key={index} event={event} />
      ))}
    </div>
  );
};

export default EventList;
