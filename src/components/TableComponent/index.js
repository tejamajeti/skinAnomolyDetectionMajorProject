import React from 'react';

import "./index.css";

const TableComponent = (props) => {
    const { data } = props;
  return (
    <div className="table-container">
      <table className="table">
        <thead className="table-head">
          <tr>
            <th> Model </th>
            <th> Disease Name </th>
            <th> Probability </th>
          </tr>
        </thead>
        <tbody>
            <tr className="table-row">
                <td> CNN </td>
                <td>{data.mobilenet_class}</td>
                <td>{data.mobilenet_prob}</td>
            </tr>
            <tr className="table-row">
                <td> DENSENET </td>
                <td>{data.densenet_class}</td>
                <td>{data.densenet_prob}</td>
            </tr>
            <tr className="table-row">
                <td> MOBILENET  </td>
                <td>{data.cnn_class}</td>
                <td>{data.cnn_prob}</td>
            </tr>
        </tbody>
      </table>
    </div>
  );
};

export default TableComponent;
