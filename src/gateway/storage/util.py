import pika, json
import logging

def upload(f, fs, channel, access):
    logging.warning("Testing123")
    try:
        fid = fs.put(f)
    except Exception as err:
        print(err)
        logging.warning("Testing444")
        return "internal server error123", 5001
    
    logging.warning("zzzzzztesting")

    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }
    logging.warning("blahbljhaljsdf")

    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
        print("Testing123")

    except Exception as err:
        print(err)
        logging.warning("hellowlrd")
        logging.warning(err)
        fs.delete(fid)
        return "internal server errorzzzz", 5002
