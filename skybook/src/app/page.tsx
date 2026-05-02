import { SearchHero } from "@/components/flights/SearchHero";
import { FlightResults } from "@/components/flights/FlightResults";
import { Suspense } from "react";

export default function HomePage() {
  return (
    <div>
      {/* Оборачиваем ОБА компонента в один Suspense. 
        Теперь и SearchHero, и FlightResults в безопасности.
      */}
      <Suspense fallback={<FlightResultsSkeleton />}>
        <SearchHero />
        <FlightResults />
      </Suspense>
    </div>
  );
}

function FlightResultsSkeleton() {
  return (
    <div className="max-w-5xl mx-auto px-6 py-8">
      {[1, 2, 3].map((i) => (
        <div key={i} className="bg-white rounded-xl border border-gray-200 p-5 mb-3 animate-pulse">
          <div className="flex items-center gap-4">
            <div className="w-10 h-10 bg-gray-100 rounded-lg" />
            <div className="flex-1 h-4 bg-gray-100 rounded" />
            <div className="w-24 h-6 bg-gray-100 rounded" />
          </div>
        </div>
      ))}
    </div>
  );
}