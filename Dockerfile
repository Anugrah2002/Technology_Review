FROM wlserver1/ytupload:latest
ADD ./ /
RUN pip3 install cloudinary
RUN pip3 install selenium
RUN python3 views.py
