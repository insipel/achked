#include <stdio.h>

typedef unsigned int uint32_t;
 

#define __BIG_ENDIAN__ 0

#if __BIG_ENDIAN__
/** post-teu pd word 0 */
typedef union post_teu_pd_w0_u {
    struct {
        uint32_t msg_id                    : 8;     /**< Software Message Id */
        uint32_t cdu_count                 : 6;     /**< Number of CDUs */
        uint32_t r_s_v_d1                  : 10;    /**< rsvd */
        uint32_t timestamp                 : 8;     /**< Timestamp */
    } fields; /**< fields */
    uint32_t u32; /**< unsigned 32 bit value */
} post_teu_pd_w0_t;

/** post-teu pd word 1 */
typedef union post_teu_pd_w1_u {
    struct {
        uint32_t mdu_count                 : 6;     /**< Number of MDUs */
        uint32_t xdu_type                  : 1;     /**< 1st xDU type (xdu_t) */
        uint32_t rel2end                   : 1;     /**< Release to end */
        uint32_t no_dm                     : 1;     /**< No Data Movement */
        uint32_t first_xdu_occ             : 11;    /**< First xDU Occupancy */
        uint32_t transmit_count            : 12;    /**< Total transmit count */
    } fields; /**< fields */
    uint32_t u32; /**< unsigned 32 bit value */
} post_teu_pd_w1_t;

/** post-teu pd word 2 */
typedef union post_teu_pd_w2_u {
    struct {
        uint32_t first_xdu_size            : 2;     /**< First xDU Size (xdu_sz_t) */
        uint32_t pkt_length                : 14;    /**< Packet Length */
        uint32_t r_s_v_d2                  : 3;     /**< rsvd */
        uint32_t ig                        : 2;     /**< Isolation Group (IG) */
        uint32_t rcos                      : 3;     /**< Resource Class of Service (RCOS) */
        uint32_t pkt_ptr_rid               : 8;     /**< Packet Ptr Region Id (RID) */
    } fields; /**< fields */
    uint32_t u32; /**< unsigned 32 bit value */
} post_teu_pd_w2_t;

/** post-teu pd word 3 */
typedef union post_teu_pd_w3_u {
    struct {
        uint32_t pkt_ptr_offset            : 32;    /**< Packet Ptr Offset */
    } fields; /**< fields */
    uint32_t u32; /**< unsigned 32 bit value */
} post_teu_pd_w3_t;

/** post-teu pd word 4 */
typedef union post_teu_pd_w4_u {
    struct {
        uint32_t ode_cmd                   : 4;     /**< Ouput DMA Engine (ODE) Command */
        uint32_t r_s_v_d3                  : 6;     /**< rsvd */
        uint32_t qid                       : 22;    /**< Queue Identifier (QID). */
    } fields; /**< fields */
    uint32_t u32; /**< unsigned 32 bit value */
} post_teu_pd_w4_t;

/** post-teu pd word 5 */
typedef union post_teu_pd_w5_u {
    struct {
        uint32_t roc_cmd                   : 4;     /**< Reorder Context (ROC) manager Command; enum: roc_command_t*/
        uint32_t r_s_v_d4                  : 4;     /**< rsvd */
        uint32_t roc_ig_credit             : 1;     /**< ROC Ignore Credit */
        uint32_t roc_dest_type             : 1;     /**< ROC Destination Type: enum: roc_destination_type_t */
        uint32_t roc_dest_addr_id          : 6;     /**< ROC Destination Identifier */
        uint32_t r_s_v_d5                  : 4;     /**< rsvd */
        uint32_t roc_gid                   : 12;    /**< ROC Global Identifier (GID) */
    } fields; /**< fields */
    uint32_t u32; /**< unsigned 32 bit value */
} post_teu_pd_w5_t;

/** post-teu pd word 6 */
typedef union post_teu_pd_w6_u {
    struct {
        uint32_t r_s_v_d6                  : 6;     /**< rsvd */
        uint32_t roc_ras_rcid              : 10;    /**< ROC Reassign Context ID */
        uint32_t r_s_v_d7                  : 6;     /**< rsvd */
        uint32_t roc_cur_rcid              : 10;    /**< ROC Current Context ID */
    } fields; /**< fields */
    uint32_t u32; /**< unsigned 32 bit value */
} post_teu_pd_w6_t;

/** post-teu pd word 7 */
typedef union post_teu_pd_w7_u {
    struct {
        uint32_t ode_transmit_cnt_update   : 12;    /**< ODE Transmit Count Update */
        uint32_t ode_mdu_count             : 6;     /**< ODE->AAM MDU Count */
        uint32_t ode_cdu_count             : 6;     /**< ODE->AAM CDU Count */
        uint32_t r_s_v_d8                  : 3;     /**< rsvd */
        uint32_t ode_ig                    : 2;     /**< ODE->AAM Isolation Group (IG) */
        uint32_t ode_rcos                  : 3;     /**< ODE->AAM RCOS */
    } fields; /**< fields */
    uint32_t u32; /**< unsigned 32 bit value */
} post_teu_pd_w7_t;

#else
/** post-teu pd word 0 */
typedef union post_teu_pd_w0_u {
    struct {
        uint32_t timestamp                 : 8;     /**< Timestamp */
        uint32_t r_s_v_d1                  : 10;    /**< rsvd */
        uint32_t cdu_count                 : 6;     /**< Number of CDUs */
        uint32_t msg_id                    : 8;     /**< Software Message Id */
    } fields; /**< fields */
    uint32_t u32; /**< unsigned 32 bit value */
} post_teu_pd_w0_t;

/** post-teu pd word 1 */
typedef union post_teu_pd_w1_u {
    struct {
        uint32_t transmit_count            : 12;    /**< Total transmit count */
        uint32_t first_xdu_occ             : 11;    /**< First xDU Occupancy */
        uint32_t no_dm                     : 1;     /**< No Data Movement */
        uint32_t rel2end                   : 1;     /**< Release to end */
        uint32_t xdu_type                  : 1;     /**< 1st xDU type (xdu_type_e) */
        uint32_t mdu_count                 : 6;     /**< Number of MDUs */
    } fields; /**< fields */
    uint32_t u32; /**< unsigned 32 bit value */
} post_teu_pd_w1_t;

/** post-teu pd word 2 */
typedef union post_teu_pd_w2_u {
    struct {
        uint32_t pkt_ptr_rid               : 8;     /**< Packet Ptr Region Id (RID)*/
        uint32_t rcos                      : 3;     /**< Resource Class of Service (RCOS) */
        uint32_t ig                        : 2;     /**< Isolation Group (IG) */
        uint32_t r_s_v_d2                  : 3;     /**< rsvd */
        uint32_t pkt_length                : 14;    /**< Packet Length */
        uint32_t first_xdu_size            : 2;     /**< First xDU Size (xdu_size_e) */
    } fields; /**< fields */
    uint32_t u32; /**< unsigned 32 bit value */
} post_teu_pd_w2_t;

/** post-teu pd word 3 */
typedef union post_teu_pd_w3_u {
    struct {
        uint32_t pkt_ptr_offset            : 32;    /**< Packet Ptr Offset*/
    } fields; /**< fields */
    uint32_t u32; /**< unsigned 32 bit value */
} post_teu_pd_w3_t;

/** post-teu pd word 4 */
typedef union post_teu_pd_w4_u {
    struct {
        uint32_t qid                       : 22;    /**< Queue Identifier (QID). */
        uint32_t r_s_v_d3                  : 6;     /**< rsvd */
        uint32_t ode_cmd                   : 4;     /**< Ouput DMA Engine (ODE) Command*/
    } fields; /**< fields */
    uint32_t u32; /**< unsigned 32 bit value */
} post_teu_pd_w4_t;

/** post-teu pd word 5 */
typedef union post_teu_pd_w5_u {
    struct {
        uint32_t roc_gid                   : 12;    /**< ROC Global Identifier (GID) */
        uint32_t r_s_v_d5                  : 4;     /**< rsvd */
        uint32_t roc_dest_addr_id          : 6;     /**< ROC Output Destination Identifier */
        uint32_t roc_dest_type             : 1;     /**< ROC Destination Type : enum: roc_destination_type_t */
        uint32_t roc_ig_credit             : 1;     /**< ROC Ignore Credit */
        uint32_t r_s_v_d4                  : 4;     /**< rsvd */
        uint32_t roc_cmd                   : 4;     /**< Reorder Context (ROC) manager command; enum: roc_command_t*/
    } fields; /**< fields */
    uint32_t u32; /**< unsigned 32 bit value */
} post_teu_pd_w5_t;

/** post-teu pd word 6 */
typedef union post_teu_pd_w6_u {
    struct {
        uint32_t roc_cur_rcid              : 10;    /**< ROC Current Context ID */
        uint32_t r_s_v_d7                  : 6;     /**< rsvd */
        uint32_t roc_ras_rcid              : 10;    /**< ROC Reassign Context ID */
        uint32_t r_s_v_d6                  : 6;     /**< rsvd */
    } fields; /**< fields */
    uint32_t u32; /**< unsigned 32 bit value */
} post_teu_pd_w6_t;

/** post-teu pd word 7 */
typedef union post_teu_pd_w7_u {
    struct {
        uint32_t ode_rcos                  : 3;     /**< ODE->AAM RCOS */
        uint32_t ode_ig                    : 2;     /**< ODE->AAM Isolation Group (IG) */
        uint32_t r_s_v_d8                  : 3;     /**< rsvd */
        uint32_t ode_cdu_count             : 6;     /**< ODE->AAM CDU Count */
        uint32_t ode_mdu_count             : 6;     /**< ODE->AAM MDU Count */
        uint32_t ode_transmit_cnt_update   : 12;    /**< ODE Transmit Count Update */
    } fields; /**< fields */
    uint32_t u32; /**< unsigned 32 bit value */
} post_teu_pd_w7_t;
#endif



typedef struct post_teu_pd_s {
    post_teu_pd_w0_t wd_0; /**< word 0 */
    post_teu_pd_w1_t wd_1; /**< word 1 */
    post_teu_pd_w2_t wd_2; /**< word 2 */
    post_teu_pd_w3_t wd_3; /**< word 3 */
    post_teu_pd_w4_t wd_4; /**< word 4 */
    post_teu_pd_w5_t wd_5; /**< word 5 */
    post_teu_pd_w6_t wd_6; /**< word 6 */
    post_teu_pd_w7_t wd_7; /**< word 7 */
} post_teu_pd_t;



int
main()
{
    post_teu_pd_t pd;
    unsigned char temp[] = {0x1c,0x98,0x00,0x25,0x00,0x08,0x60,0x01,
                            0x23,0x24,0x09,0xee,0x00,0x0d,0x33,0x7a,
                            0x00,0x00,0x00,0x00,0x00,0x00,0x0f,0xe1,
                            0x00,0x00,0x02,0xde,0x00,0x00,0x26,0x09};
    unsigned int temp32[] = {0x1c980025,0x00086001,
                           0x232409ee,0x000d337a,
                           0x00000000,0x00000fe1,
                           0x000002de,0x00002609};

    pd = *((post_teu_pd_t *)temp32);

    printf("pd:wd_0 msg_id:0x%x,cdu_count:0x%x,r_s_v_d1:0x%x,timestamp:0x%x,\n\n",pd.wd_0.fields.msg_id,pd.wd_0.fields.cdu_count,pd.wd_0.fields.r_s_v_d1,pd.wd_0.fields.timestamp);

    printf("pd:wd_1 mdu_count:0x%x,xdu_type:0x%x,rel2end:0x%x,no_dm:0x%x,first_xdu_occ:0x%x,transmit_count:0x%x,\n\n",pd.wd_1.fields.mdu_count,pd.wd_1.fields.xdu_type,pd.wd_1.fields.rel2end,pd.wd_1.fields.no_dm,pd.wd_1.fields.first_xdu_occ,pd.wd_1.fields.transmit_count);

    printf("pd:wd_2 first_xdu_size:0x%x,pkt_length:0x%x,r_s_v_d2:0x%x,ig:0x%x,rcos:0x%x,pkt_ptr_rid:0x%x,\n\n",pd.wd_2.fields.first_xdu_size,pd.wd_2.fields.pkt_length,pd.wd_2.fields.r_s_v_d2,pd.wd_2.fields.ig,pd.wd_2.fields.rcos,pd.wd_2.fields.pkt_ptr_rid);

    printf("pd:wd_3 pkt_ptr_offset:0x%x,\n\n",pd.wd_3.fields.pkt_ptr_offset);

    printf("pd:wd_4 ode_cmd:0x%x,r_s_v_d3:0x%x,qid:0x%x,\n\n",pd.wd_4.fields.ode_cmd,pd.wd_4.fields.r_s_v_d3,pd.wd_4.fields.qid);

    printf("pd:wd_5 roc_cmd:0x%x,r_s_v_d4:0x%x,roc_ig_credit:0x%x,roc_dest_type:0x%x,roc_dest_addr_id:0x%x,r_s_v_d5:0x%x,roc_gid:0x%x,\n\n",pd.wd_5.fields.roc_cmd,pd.wd_5.fields.r_s_v_d4,pd.wd_5.fields.roc_ig_credit,pd.wd_5.fields.roc_dest_type,pd.wd_5.fields.roc_dest_addr_id,pd.wd_5.fields.r_s_v_d5,pd.wd_5.fields.roc_gid);

    printf("pd:wd_6 r_s_v_d6:0x%x,roc_ras_rcid:0x%x,r_s_v_d7:0x%x,roc_cur_rcid:0x%x,\n\n",pd.wd_6.fields.r_s_v_d6,pd.wd_6.fields.roc_ras_rcid,pd.wd_6.fields.r_s_v_d7,pd.wd_6.fields.roc_cur_rcid);

    printf("pd:wd_7 ode_transmit_cnt_update:0x%x,ode_mdu_count:0x%x,ode_cdu_count:0x%x,r_s_v_d8:0x%x,ode_ig:0x%x,ode_rcos:0x%x,\n\n",pd.wd_7.fields.ode_transmit_cnt_update,pd.wd_7.fields.ode_mdu_count,pd.wd_7.fields.ode_cdu_count,pd.wd_7.fields.r_s_v_d8,pd.wd_7.fields.ode_ig,pd.wd_7.fields.ode_rcos);
}

