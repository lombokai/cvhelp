def combine_tocenter(src_image, dst_image):
    ''' Combine two image to be one single image '''
    # get shape
    bh, bw, _ = dst_image.shape
    sh, sw, _ = src_image.shape

    # get center
    lh = int((bh - sh) / 2 )  
    lw = int((bw - sw) / 2) 
    rh = bh - lh
    rw = bw - lw

    #normalize dimension error if dimension is not match
    new_img = dst_image
    nh, nw, _ = dst_image[lh:rh, lw:rw].shape

    #find difference dimension between new shape and replacement image
    kh = nh - sh
    kw = nw - sw

    #normalize dimension dimension
    rh = rh - kh
    rw = rw - kw

    #Replace Image in center
    new_img[lh:rh, lw:rw] = src_image
    return new_img

