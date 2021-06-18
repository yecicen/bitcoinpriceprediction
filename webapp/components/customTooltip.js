const CustomTooltip = ({ active, payload }) => {
    if (active && payload && payload.length) {
      return (
        <div className="bg-gray-100">
          <p className="text-white">{`${payload[0].payload["date"]}`}</p>
          <p className="text-purple-300	">{`${payload[0].payload["price"]}`}</p>
          <p className="label">{`${payload[0].payload["prediction"]}`}</p>
          <p className="label">{`${payload[0].payload["difference"]}`}</p>
        </div>
      );
    }
  
    return null;
  };
  export default CustomTooltip;