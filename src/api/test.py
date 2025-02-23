from dotenv import load_dotenv

from contoso_chat.chat_request import get_response
load_dotenv()


from prompty.tracer import trace, Tracer, console_tracer, PromptyTracer


# add console and json tracer:
# this only has to be done once
# at application startup
Tracer.add("console", console_tracer)
json_tracer = PromptyTracer()
Tracer.add("PromptyTracer", json_tracer.tracer)



if __name__ == "__main__":
    from tracing import init_tracing

    tracer = init_tracing(local_tracing=False)
    get_response(4, "What hiking jackets would you recommend?", [])
    #get_response(argv[1], argv[2], argv[3])