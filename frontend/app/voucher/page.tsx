import React from "react";

const VoucherPage = () => {
  return (
    <form>
      <div className="form-group text-center fw-bolder">
        <label htmlFor="name">Name</label>
        <input
          type="text"
          className="form-control"
          id="name"
          placeholder="Enter name"
        />
      </div>
      <div className="form-group text-center fw-bolder">
        <label htmlFor="startDate">Start Date</label>
        <input
          type="date"
          className="form-control"
          id="startDate"
          placeholder="Enter start date"
        />
      </div>
      <div className="form-group text-center fw-bolder">
        <label htmlFor="endDate">End Date</label>
        <input
          type="date"
          className="form-control"
          id="endDate"
          placeholder="Enter end date"
        />
      </div>
      <div className="form-group text-center fw-bolder">
        <label htmlFor="code">Code</label>
        <input
          type="text"
          className="form-control"
          id="code"
          placeholder="Enter code"
        />
      </div>
    </form>
  );
};

export default VoucherPage;
