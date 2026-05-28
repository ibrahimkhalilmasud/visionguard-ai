const layouts = [1, 4, 9, 16];

export default function DashboardPage() {
  return (
    <main className="min-h-screen p-6 space-y-6">
      <header className="flex items-center justify-between">
        <h1 className="text-3xl font-bold">VisionGuard-AI Dashboard</h1>
        <span className="rounded bg-emerald-600 px-3 py-1 text-sm">System Healthy</span>
      </header>

      <section>
        <h2 className="mb-3 text-xl font-semibold">Camera Grid Layouts</h2>
        <div className="grid grid-cols-4 gap-3">
          {layouts.map((layout) => (
            <div key={layout} className="rounded border border-gray-700 p-3">
              {layout}-camera layout
            </div>
          ))}
        </div>
      </section>

      <section className="grid grid-cols-1 gap-4 lg:grid-cols-2">
        <div className="rounded border border-gray-700 p-4">
          <h2 className="text-lg font-semibold">Live Event Feed</h2>
          <p className="text-sm text-gray-300">No events in the last minute.</p>
        </div>
        <div className="rounded border border-gray-700 p-4">
          <h2 className="text-lg font-semibold">Threat Analytics</h2>
          <p className="text-sm text-gray-300">Inference latency target: &lt; 300ms.</p>
        </div>
      </section>
    </main>
  );
}
