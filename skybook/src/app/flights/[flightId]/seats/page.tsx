import { SeatMap } from "@/components/seats/SeatMap";
import { FlightHeader } from "@/components/seats/FlightHeader";

export default function SeatsPage({ params }: { params: { flightId: string } }) {
  const flightId = parseInt(params.flightId);
  return (
    <div className="max-w-6xl mx-auto px-6 py-6">
      <FlightHeader flightId={flightId} />
      <SeatMap flightId={flightId} />
    </div>
  );
}
