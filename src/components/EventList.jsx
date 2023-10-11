import React, { useState } from "react";
import data from "../assets/data.json";

// EventBox is a React component that displays information about an event.
const EventBox = ({ event }) => {
  // Define a state variable "expanded" and a function "setExpanded" to toggle the description.
  const [expanded, setExpanded] = useState(false);

  // Function to toggle the description's visibility.
  const toggleDescription = () => {
    setExpanded(!expanded);
  };

  return (
    <div className="border-2 border-black">
      <div
        // Apply dynamic CSS classes for styling and animation based on "expanded" state.
        className={`bg-white rounded-lg w-72 p-6 m-4 flex flex-col transform hover:scale-105 transition-transform duration-300 ease-in-out shadow-m ${
          expanded ? "h-auto" : "h-72"
        } overflow-hidden`}
      >
        <h2 className="text-2xl font-bold mb-2 text-red-600">{event.name}</h2>
        <p className="text-gray-500">
          {event.startsOn} - {event.endsOn}
          <br />
          Hosted by: {event.organizationName}
        </p>
        <div className={`text-gray-800 mt-2 ${expanded ? "" : "truncate"}`}>
          {/* Display either full description or a truncated version based on "expanded" state. */}
          {expanded ? event.description : event.description.substring(0, 100)}
        </div>
        {/* Display "Read More" button only if the description is longer than 100 characters and not expanded. */}
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

// renders a list of events using the EventBox component.
const EventList = () => {
  return (
    <div className="flex flex-wrap gap-6 justify-center">
      {data.map((event, index) => (
        // Render the EventBox component for each event in the data array.
        <EventBox key={index} event={event} />
      ))}
    </div>
  );
};

export default EventList; // Export the EventList component
