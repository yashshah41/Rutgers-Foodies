import React from 'react'
import PropTypes from 'prop-types'
import jsonString from '../assets/data.json'
import './EventList.css'

const EventBox = ({ event }) => (
  <div className="event-box">
    <h2>{event.name}</h2>
    <p>Date: {event.startsOn} - {event.endsOn}<p>
    </p> Description: {event.description} </p>
    {/* Add more fields as needed */}
  </div>
);

const EventList = (props) => {
  const data = JSON.parse(JSON.stringify(jsonString));

  return (
    <div className="event-list">
      {data.map((event, index) => (
        <EventBox key={index} event={event} />
      ))}
    </div>
  );
}

EventList.propTypes = {}

export default EventList
