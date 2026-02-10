export default {
  async fetch(request, env) {
    try {
      const body = await request.json();
      const prompt = body.prompt;

      const result = await env.AI.run(
        "@cf/mistral/mistral-7b-instruct",
        {
          messages: [
            { role: "system", content: "Rewrite the prompt clearly." },
            { role: "user", content: prompt }
          ]
        }
      );

      return new Response(
        JSON.stringify({ ok: true, result }),
        { status: 200, headers: { "Content-Type": "application/json" } }
      );
    } catch (err) {
      return new Response(
        JSON.stringify({
          ok: false,
          error: err?.message || String(err),
          stack: err?.stack || null
        }),
        { status: 500, headers: { "Content-Type": "application/json" } }
      );
    }
  }
};
